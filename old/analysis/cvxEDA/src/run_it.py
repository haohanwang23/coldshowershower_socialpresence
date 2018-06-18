import cvxEDA

import pandas as pd
import numpy as np
import pylab as pl

df = pd.read_csv('EDAnumpy.csv')

hw_eda = np.asarray(df.iloc[:,0])
y = hw_eda

yn = (y - y.mean()) / y.std()
Fs = 4.
[r, p, t, l, d, e, obj] = cvxEDA.cvxEDA(yn, 1./Fs)
tm = pl.arange(1., len(y)+1.) / Fs
pl.hold(True)
pl.plot(tm, yn)
pl.plot(tm, r)
pl.plot(tm, p)
pl.plot(tm, t)

pl.savefig('foo.png')
pl.savefig('foo.pdf')