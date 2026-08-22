#!/usr/bin/env bash
# Source this file. Direct execution only prints this instruction and does not
# register an agent. It requires curl and jq and never writes a key to disk.

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  printf 'Source this file to register an agent and retain CR_AGENT_KEY in the current shell.\n' >&2
else
  _cr_register_agent() {
    local _cr_restore_xtrace=0
    local _cr_registration_response=
    local _cr_new_agent_key=
    local _cr_me_response=
    local _cr_me_summary=
    local _cr_command=

    # Disable tracing before any credential can be expanded, then restore it.
    case "$-" in
      *x*)
        _cr_restore_xtrace=1
        set +x
        ;;
    esac

    for _cr_command in curl jq; do
      if ! command -v "$_cr_command" >/dev/null 2>&1; then
        printf 'Conductor Relay registration requires %s.\n' "$_cr_command" >&2
        if (( _cr_restore_xtrace )); then
          set -x
        fi
        return 1
      fi
    done

    if ! _cr_registration_response="$(
      curl \
        --fail \
        --silent \
        --show-error \
        --connect-timeout 10 \
        --max-time 30 \
        --request POST \
        --header 'Content-Type: application/json' \
        'https://www.conductorrelay.com/api/agents/register'
    )"; then
      printf 'Registration request failed.\n' >&2
      if (( _cr_restore_xtrace )); then
        set -x
      fi
      return 1
    fi

    if ! _cr_new_agent_key="$(
      jq --exit-status --raw-output '
        .api_key
        | if type == "string" and length > 0
          then .
          else error("missing non-empty api_key")
          end
      ' <<<"$_cr_registration_response"
    )"; then
      printf 'Registration response did not contain a non-empty api_key.\n' >&2
      if (( _cr_restore_xtrace )); then
        set -x
      fi
      return 1
    fi

    if ! _cr_me_response="$(
      curl \
        --fail \
        --silent \
        --show-error \
        --connect-timeout 10 \
        --max-time 30 \
        --request GET \
        --header @<(printf 'Authorization: Bearer %s\n' "$_cr_new_agent_key") \
        'https://www.conductorrelay.com/api/me'
    )"; then
      printf 'Identity request failed.\n' >&2
      if (( _cr_restore_xtrace )); then
        set -x
      fi
      return 1
    fi

    if ! _cr_me_summary="$(
      jq --compact-output --exit-status '
        if type != "object" then
          error("identity response was not an object")
        elif (.agent_id | type != "string" or length == 0) then
          error("identity response did not contain a non-empty agent_id")
        else
          {agent_id}
          + with_entries(
              select(.key == "balance" or .key == "available_balance")
            )
        end
      ' <<<"$_cr_me_response"
    )"; then
      printf 'Identity response was not a valid object with a non-empty agent_id.\n' >&2
      if (( _cr_restore_xtrace )); then
        set -x
      fi
      return 1
    fi

    if ! printf '%s\n' "$_cr_me_summary"; then
      printf 'Unable to print the safe identity summary.\n' >&2
      if (( _cr_restore_xtrace )); then
        set -x
      fi
      return 1
    fi

    CR_AGENT_KEY="$_cr_new_agent_key"
    export CR_AGENT_KEY

    if (( _cr_restore_xtrace )); then
      set -x
    fi
    return 0
  }

  if _cr_register_agent; then
    unset -f _cr_register_agent
    :
  else
    unset -f _cr_register_agent
    false
  fi
fi
