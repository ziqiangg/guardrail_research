#!/bin/bash
cd "C:/Users/cys-c/Desktop/gzqr/gitubrepo/misc/researchrail/guardrail_research"
S=benchtest/scratchpad/url-checker/purplellama
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
: > $S/codes.txt
while IFS= read -r url; do
  [ -z "$url" ] && continue
  if [[ "$url" == *files.pythonhosted.org* ]]; then M="-I"; else M=""; fi
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 25 $M -A "$UA" "$url")
  if [ "$code" = "000" ]; then sleep 2; code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 25 $M -A "$UA" "$url"); fi
  echo "$code $url" >> $S/codes.txt
  if [[ "$url" == *github.com* ]]; then sleep 1.5; fi
done < $S/urls_unique.txt
echo DONE >> $S/codes.txt
