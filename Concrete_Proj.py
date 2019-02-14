# -*- coding: utf-8 -*-
#%%
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
sns.set(color_codes=True)
from scipy import stats
#%%
conc = pd.read_csv("Concrete_Data_Yeh.csv")

#%%
cols = list(conc.columns)
cols.pop()
#['cement', 'slag', 'flyash', 'water', 'superplasticizer', 'coarseaggregate', 'fineaggregate', 'age', 'csMPa']

#%%

desc = conc.describe()

#%%
sns.distplot(conc['csMPa'])

#%%
fig, axs = plt.subplots(ncols=8)
sns.distplot(conc['age'], ax=axs[0])
sns.distplot(conc['cement'], ax=axs[0])

cols = list(zip( cols, range(0,8)))

fig, axs = plt.subplots(ncols=len(cols))

for f, a in cols:
    sns.distplot(conc[f], ax=axs[a])

fig.set_size_inches(12, 12)
fig.savefig('mats_distro.png')
#%%


