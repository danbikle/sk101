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
cdate_l = [datetime.datetime.strptime(row, "%Y-%m-%d") for row in df1['cdate'].values]
cp_l    = [row for row in df1['cp']] 
cplead_l = cp_l + [cp_l[-1]]
cplead_l = cplead_l[1:]

delta_a = np.array(cplead_l) - np.array(cp_l)
delta_l = [elm for elm in delta_a]

# I should avoid most recent delta_l since I dont know it yet.
delta_l   = delta_l[:-1]
cp_mirror = [cp_l[0]]
green_l   = [cp_l[0]]

# I should get my predictions
prediction_l = [prediction for row in df1['prediction']]

# I should work on the green line
cp_i = 0
for delta in delta_l:
  green_pt    = green_l[cp_i]
  prediction  = prediction_l[cp_i]
  green_delta = delta * np.sign(prediction)
  green_l.append(green_pt + green_delta)
  cp_i += 1
pdb.set_trace()

len(green_l) == len(cp_l)

# actually I might want this:
plt.plot(cdate_l, cp_l, 'b-')

plt.savefig('/tmp/myfig')
plt.close()


'bye'
