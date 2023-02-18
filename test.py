#!/bin/python3
import os
from os import path
import sys
from datetime import datetime
import json

with open('package.json') as js:
  for k, v in json.load(js).items():
    print(f'..key:value: {k}:{v}')