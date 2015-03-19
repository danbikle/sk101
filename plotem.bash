#!/bin/bash

# /home/ann/sk101/plotem.bash

# This script should plot data in a CSV file

# Demo:
# /home/ann/sk101/plotem.bash /tmp/sk101/prdf1.csv

if [ $# -ne 1 ]
then
  echo I need 1 arg.
  echo Demo:
  echo $0 /tmp/sk101/prdf1.csv
  exit 1
fi

echo Working...

python /home/ann/sk101/plotem.py $1

exit
