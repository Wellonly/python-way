#!/bin/python3
""" Stub with logging for a file(executable) by execute instead a target file.
Usage: install this file instead a target. It'll only log its arguments when called with datatime stamp.
       A notify(x11) will be raised if libnotify-bin installed on the system
License: MIT License, Copyright (c) 2023, github.com/Wellonly
"""
import os
from os import path
import sys
from datetime import datetime

logdir = '/tmp/log'
if not path.exists(logdir): os.mkdir(logdir)
with open(f'{logdir}/{path.basename(__file__)}.txt', '+a') as file:
  file.write(" ".join([datetime.now().strftime('%Y.%m.%d-%H:%M:%S'), 'argv:', ' '.join(sys.argv),"\n"]))
os.system(f"notify-send '..file updated: {file.name}'")