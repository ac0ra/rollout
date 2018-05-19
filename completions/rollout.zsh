if [[ ! -o interactive ]]; then
    return
fi

compctl -K _rollout rollout

_rollout() {
  local word words completions
  read -cA words
  word="${words[2]}"

  if [ "${#words}" -eq 2 ]; then
    completions="$(rollout commands)"
  else
    completions="$(rollout completions "${word}")"
  fi

  reply=("${(ps:\n:)completions}")
}
