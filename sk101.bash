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

# I should generate features
cd /tmp/sk101/

for TKR in XOM MDY GSPC
do
  python ~ann/sk101/genf.py      ${TKR}2.csv
  grep -v cdate ftr${TKR}2.csv > ${TKR}3.csv
done

# I should create wide1.csv
sqlite3 sk101.db '.read /home/ann/sk101/joinem.sql'

# I should predict
python ~ann/sk101/sk101.py

cd ~ann/sk101/

# I should plot blue-line-green-line
python plotem.py /tmp/sk101/prdf1.csv
python plotem.py /tmp/sk101/prdf3.csv
python plotem.py /tmp/sk101/prdf4.csv
python plotem.py /tmp/sk101/prdf5.csv
python plotem.py /tmp/sk101/prdf7.csv

exit
