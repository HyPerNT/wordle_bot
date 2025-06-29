#!/bin/bash

# Interrogate
interrogate --generate-badge badges/interrogate.svg --fail-under 80

# Pytest coverage
rm badges/coverage.svg
coverage-badge -o badges/coverage.svg
