#!/bin/bash

# /home/ann/sk101/wgetem.bash

# This script should get CSV data from Yahoo.

mkdir -p /tmp/sk101/
cd       /tmp/sk101/

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.csv

wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}
cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv

for TKR in XOM MDY
do
  echo $TKR
  rm -f ${TKR}.html ${TKR}.csv
  wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKR}
  cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv
done

exit
