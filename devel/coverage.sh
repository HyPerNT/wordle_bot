#!/bin/bash

# Coverage

coverage run -m pytest && coverage report && coverage html -d cov
