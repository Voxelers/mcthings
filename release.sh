#!/bin/sh

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# Increment version in setup.py
# Commit and tag with the new version
# Push branch with tags
# Generate pip packages and upload to pip repository
cd tests/integration
PYTHONPATH=../..:.. ./run_tests.py
cd ../..
rm dist/*
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
