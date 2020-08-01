#!/bin/bash

coverage run -a --omit=test.py test.py
coverage report -m
