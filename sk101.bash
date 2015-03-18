#!/bin/bash

# /home/ann/sk101/sk101.bash

# This script should predict GSPC.
# Ref:
# http://finance.yahoo.com/q?s=^GSPC

if [ -e ~ann/sk101/ ]; then
  echo $0 is in the correct folder.
else
  echo $0 needs to reside here:
  echo ~ann/sk101/
  echo bye.
  exit 1
fi

cd       ~ann/sk101/
mkdir -p /tmp/sk101/

# I should get csv data
./wgetem.bash

exit
