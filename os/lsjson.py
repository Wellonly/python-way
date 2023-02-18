#!/bin/python3
import sys
import json

def lsjson(argv):
  '''..usage: lsjson <file> [branch [subbranch]]; print a content of file(.json) with entries on specified branch or all content'''
  if len(argv) == 1 or argv[1] == '--help':
    print(lsjson.__doc__)
    quit(4)

  def _printDictonary(level, branch, dic):
<<<<<<< HEAD
=======
    nonlocal argv
>>>>>>> 2d91aec7f84eb487143558495bf3384cace65b9a
    for k, v in dic.items():
      if level <= 0 or k == argv[-level]:
        if type(v) == dict:
          _printDictonary(level-1, f'{branch}:{k}', v)
        else:
          print(f'{branch}:{k}:{v}')

  level=len(argv)-2
  with open(argv[1]) as js:
    for k, v in json.load(js).items():
      if level == 0 or k == argv[-level]:
        if type(v) == dict:
          _printDictonary(level-1, k, v)
        else:
          print(f'{k}:{v}')

if __name__ == '__main__':
  lsjson(sys.argv)