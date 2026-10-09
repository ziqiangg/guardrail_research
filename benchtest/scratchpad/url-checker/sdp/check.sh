#!/bin/bash
# usage: check.sh URL -> prints "<code>\t<effective_url>\t<attempt>"
u="$1"
for a in 1 2; do
  out=$(curl -s -o /dev/null -L --max-time 25 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" -w "%{http_code}\t%{url_effective}" "$u" 2>/dev/null)
  rc=$?
  code=${out%%	*}
  if [ $rc -eq 0 ] && [ "$code" != "000" ]; then echo "$out	$a"; exit 0; fi
  sleep 2
done
echo "000	$u	$rc	2"
