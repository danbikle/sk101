# ~ann/sk101/sk101.py

# This script should learn from wide1.csv and then issue predictions.

# Demo:
# cd /tmp/sk101/
# python ~ann/sk101/sk101.py

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
pcount = 252 * 1

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

# http://scikit-learn.org/stable/modules/ensemble.html#regression
# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
# http://scikit-learn.org/stable/modules/svm.html#regression

from sklearn.ensemble  import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm, linear_model

model1 = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=0, loss='ls')
model2 = KNeighborsClassifier(n_neighbors=(int(train_count)), weights='distance')
model4 = svm.SVR()
model5 = linear_model.LinearRegression()
model6 = linear_model.LogisticRegression()

# I should use a list to save my predictions
model1_predictions_l = []
model2_predictions_l = []
model2_plot_data_l   = []
model4_predictions_l = []
model5_predictions_l = []
model6_predictions_l = []
model6_plot_data_l   = []

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
    model1.fit(x_train, y_train)
    model2.fit(x_train, yc_train)
    model4.fit(x_train, y_train)
    model5.fit(x_train.astype(float), y_train.astype(float))
    model6.fit(x_train, yc_train)
  m1p     = model1.predict(x_oos)[0]
  m2p     = model2.predict_proba(x_oos)[0,1]
  m4p     = model4.predict(x_oos)[0]
  m5p     = model5.predict(x_oos)
  m6p     = model6.predict_proba(x_oos.astype(float))[0,1]
  pctlead = wide_a[oos_i,pctlead_i]
  cp      = wide_a[oos_i,cp_i     ]
  model1_predictions_l.append([pdate, cp, m1p,     pctlead])
  model2_predictions_l.append([pdate, cp, m2p,     pctlead])
  model2_plot_data_l.append(  [pdate, cp, m2p-0.5, pctlead])
  model4_predictions_l.append([pdate, cp, m4p,     pctlead])
  model5_predictions_l.append([pdate, cp, m5p,     pctlead])
  model6_predictions_l.append([pdate, cp, m6p,     pctlead])
  model6_plot_data_l.append(  [pdate, cp, m6p-0.5, pctlead])

prdf1 = pd.DataFrame(model1_predictions_l)
prdf2 = pd.DataFrame(model2_predictions_l)
prdf3 = pd.DataFrame(model2_plot_data_l  )
prdf4 = pd.DataFrame(model4_predictions_l)
prdf5 = pd.DataFrame(model5_predictions_l)
prdf6 = pd.DataFrame(model6_predictions_l)
prdf7 = pd.DataFrame(model6_plot_data_l  )

for df in [prdf1,prdf2,prdf3,prdf4,prdf5,prdf6,prdf7]:
  df.columns = ['cdate','cp','prediction','actual']

# I should save my work
prdf1.to_csv('prdf1.csv', float_format='%4.3f', index=False)
prdf2.to_csv('prdf2.csv', float_format='%4.3f', index=False)
prdf3.to_csv('prdf3.csv', float_format='%4.3f', index=False)
prdf4.to_csv('prdf4.csv', float_format='%4.3f', index=False)
prdf5.to_csv('prdf5.csv', float_format='%4.3f', index=False)
prdf6.to_csv('prdf6.csv', float_format='%4.3f', index=False)
prdf7.to_csv('prdf7.csv', float_format='%4.3f', index=False)
print('I have saved predictions in prdf1.csv')
print('I have saved predictions in prdf2.csv')
print('I have saved predictions in prdf3.csv')
print('I have saved predictions in prdf4.csv')
print('I have saved predictions in prdf5.csv')
print('I have saved predictions in prdf6.csv')
print('I have saved predictions in prdf7.csv')

'bye'
