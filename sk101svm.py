# ~ann/sk101/sk101svm.py

# This script should learn from wide1.csv and then issue predictions.

# Demo:
# cd /tmp/sk101/
# python ~ann/sk101/sk101svm.py

import pdb
import pandas as pd
import numpy  as np
import sys

df1 = pd.read_csv('wide1.csv')

# How many observations have I?
obs_count = len(df1)
print('I have this many observations: '+str(obs_count))

# I should get this many predictions:
pcount = 2390 # Near the max

# I should learn from this many observations:
train_count = 252 * 10

if pcount + train_count > obs_count:
  print('You need to lower pcount and-or train_count.')
  sys.exit()
  
# I should get some training data from df1.
# I should put it in NumPy Arrays.

number_of_rows    = len(df1)
number_of_columns = len(df1.columns)

# I should declare some integers to help me navigate the Arrays.
# The layout and names of the columns are specified by joinem.sql:

cdate_i   = 0
cp_i      = 1
pctlead_i = 2
dow_i     = 3
dom_i     = 4
moy_i     = 5
mdy4_i    = 6

# I should use plain integers for the remaining 40 columns.

wide_a = np.array(df1)
x_a    = wide_a[:,dow_i:   ]
y_a    = wide_a[:,pctlead_i]

# Ref:
# http://scikit-learn.org/stable/modules/svm.html#regression
from sklearn import svm

model4 = svm.SVR()

# I should use a list to save my predictions
model4_predictions_l = []

# I should build a prediction loop from pcount.
# Higher dofit means fewer models means faster loop:
dofit = 10
# I should have this number of days between training data and oos data:
train_oos_gap = dofit # train_oos_gap should <= dofit
# Larger train_oos_gap means less precision.

for oos_i in range(0,pcount):
  print('Busy with prediction calculation: '+str(oos_i+1))
  x_oos       = x_a[oos_i,:]
  train_start = oos_i+1+train_oos_gap
  train_end   = train_start + train_count
  x_train     = x_a[train_start:train_end]
  y_train     = y_a[train_start:train_end]
  yc_train    = y_train > np.mean(y_train)

  pdate   = wide_a[oos_i,cdate_i]
  if oos_i % dofit == 0:
    model4.fit(x_train, y_train)
  m4p     = model4.predict(x_oos)[0]
  pctlead = wide_a[oos_i,pctlead_i]
  cp      = wide_a[oos_i,cp_i     ]
  model4_predictions_l.append([pdate, cp, m4p,     pctlead])

prdf4 = pd.DataFrame(model4_predictions_l)
prdf4.columns = ['cdate','cp','prediction','actual']

# I should save my work
prdf4.to_csv('prdf4.csv', float_format='%4.3f', index=False)
print('I have saved predictions in prdf4.csv')


'bye'
