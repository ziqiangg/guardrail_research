#!/bin/bash
cd "C:/Users/cys-c/Desktop/gzqr/gitubrepo/misc/researchrail/guardrail_research"
S=benchtest/scratchpad/url-checker/purplellama
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
: > $S/retry_codes.txt
while IFS= read -r url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 25 -A "$UA" "$url")
  raw=$(echo "$url" | sed -E 's#https://github.com/([^/]+)/([^/]+)/blob/#https://raw.githubusercontent.com/\1/\2/#')
  rcode=""
  if [ "$raw" != "$url" ]; then sleep 3; rcode=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 25 -A "$UA" "$raw"); fi
  echo "$code $rcode $url" >> $S/retry_codes.txt
  sleep 8
done < $S/gh_retry.txt
echo DONE >> $S/retry_codes.txt
