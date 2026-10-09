#!/bin/bash
cd /home/user/guardrail_research
export PYTHONIOENCODING=utf-8
python benchtest/tools/fetch_text.py "$2" > benchtest/scratchpad/resolver/r2/$1.txt 2>&1
head -1 benchtest/scratchpad/resolver/r2/$1.txt | cut -c1-160
