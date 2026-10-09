#!/bin/bash
# usage: get.sh name url
cd /home/user/guardrail_research
export PYTHONIOENCODING=utf-8
python benchtest/tools/fetch_text.py "$2" > benchtest/scratchpad/resolver/$1.txt 2>&1
head -1 benchtest/scratchpad/resolver/$1.txt
