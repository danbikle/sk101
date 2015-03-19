# /home/ann/sk101/plotem.py

# This script should plot data in a CSV file

# Demo:
# python /home/ann/sk101/plotem.py /tmp/sk101/prdf1.csv

import pandas as pd
import numpy  as np
import pdb
import datetime
import matplotlib
# http://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

# I should load the csv into a df

df1 = pd.read_csv(sys.argv[1]).sort(['cdate'])

# matplotlib likes dates:
plt_date = [datetime.datetime.strptime(row, "%Y-%m-%d") for row in df1['cdate'].values]

plt_cp   = [row for row in df1['cp']] 

# I dont know the outcome of most recent prediction,
# so I dont plot the most recent row:
plt.plot(plt_date[:-1], plt_cp[:-1], 'b-')

plt.savefig('/tmp/myfig')
plt.close()


'bye'
