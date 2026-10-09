#!/bin/bash
# usage: check.sh url -> prints "code|finalurl"
u="$1"
for try in 1 2; do
  out=$(curl -s -o /dev/null -L --max-time 25 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" -w "%{http_code}|%{url_effective}" "$u")
  code=${out%%|*}
  [ "$code" != "000" ] && break
  sleep 2
done
echo "$out"
