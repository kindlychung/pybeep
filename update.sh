#!/usr/bin/env bash

if [[ -e .registered ]]; then
    :
else
    python3 setup.py register
    touch .registered
fi
python3 setup.py bdist_wheel
python3 setup.py bdist_wheel upload
pip3 install $1 -U
