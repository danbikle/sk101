# /home/ann/sk101/plotem.py

# This script should plot data in a CSV file

# Demo:
# python /home/ann/sk101/plotem.py /tmp/sk101/prdf1.csv

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys

print('hello, from '+ sys.argv[0])

#  len(sys.argv) should == 2
if len(sys.argv) == 1:
  print('I need a command line arg.')
  print('Demo:')
  print('python '+sys.argv[0]+' /tmp/sk101/prdf1.csv')
  print('Try again. bye.')
  sys.exit()

print(sys.argv[1])

