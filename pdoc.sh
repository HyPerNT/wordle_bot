#!/bin/bash

(pdoc3 -f --html --output-dir docs --skip-errors src/common src/wordle src/bots src/tester > pdoc.log 2>&1 && rm -rf pdoc.log) || (echo "pdoc failed, check pdoc.log for details" && exit 1)
