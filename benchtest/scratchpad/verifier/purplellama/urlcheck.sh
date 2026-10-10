#!/bin/bash
# usage: urlcheck.sh urls.tsv > url_check.txt
REPO=benchtest/scratchpad/explorer/purplellama_code/repo
while IFS=$'\t' read -r u where; do
  case "$u" in
    https://api.*|*huggingface.co/api/*|*/v1|*/v1/*) echo "SKIP-API	$u	$where"; continue;;
  esac
  if [[ "$u" =~ ^https://github.com/([^/]+)/([^/]+)/blob/([^/]+)/(.*)$ ]]; then
    raw="https://raw.githubusercontent.com/${BASH_REMATCH[1]}/${BASH_REMATCH[2]}/${BASH_REMATCH[3]}/${BASH_REMATCH[4]}"
    s=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 40 "$raw")
    [ "$s" != "200" ] && sleep 2 && s=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 40 "$raw")
    echo "$s(raw)	$u	$where"
  elif [[ "$u" =~ ^https://github.com/meta-llama/PurpleLlama/tree/172c1074069eb88ec834124272c1b1c4f8893445/(.*)$ ]]; then
    p="${BASH_REMATCH[1]}"
    if git -C $REPO cat-file -e "172c1074:${p}" 2>/dev/null; then t=$(git -C $REPO cat-file -t "172c1074:${p}"); echo "TREE-OK($t)	$u	$where"; else echo "TREE-MISSING	$u	$where"; fi
  elif [[ "$u" == https://files.pythonhosted.org/* ]]; then
    s=$(curl -s -I -o /dev/null -w "%{http_code}" -L --max-time 40 "$u"); echo "$s(HEAD)	$u	$where"
  else
    s=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 40 -A "Mozilla/5.0" "$u")
    [ "$s" != "200" ] && sleep 2 && s=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 40 -A "Mozilla/5.0" "$u")
    echo "$s	$u	$where"
  fi
done < "$1"
