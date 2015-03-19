# /home/ann/sk101/plotem.py

# This script should plot data in a CSV file

# Demo:
# python /home/ann/sk101/plotem.py /tmp/sk101/prdf1.csv

import pandas as pd
import numpy  as np
import pdb
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

df1 = pd.read_csv(sys.argv[1])
pdb.set_trace()
df1.head()

plt.plot(df1['cdate'], df1['cp'], 'b-')
plt.savefig('/tmp/myfig')
plt.close()


'bye'
