#!/bin/sh

# Increment version in setup.py
# Commit and tag with the new version
# Push branch with tags
# Generate pip packages and upload to pip repository
tests/run_tests.py
rm dist/*
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
