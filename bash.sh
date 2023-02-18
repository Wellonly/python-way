#/bin/bash

function lsjson {
  python3 data/lsjson.py ${@:1}
}

  