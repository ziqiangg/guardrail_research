#!/bin/bash
# usage: getpage.sh <name> <url>  -> saves raw text to pages/<name>.txt
cd /home/user/guardrail_research
export PYTHONIOENCODING=utf-8
python benchtest/tools/fetch_text.py "$2" > benchtest/scratchpad/resolver/pages/$1.txt 2>&1
head -c 300 benchtest/scratchpad/resolver/pages/$1.txt | head -5
wc -l benchtest/scratchpad/resolver/pages/$1.txt
