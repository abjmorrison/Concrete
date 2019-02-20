# -*- coding: utf-8 -*-
#%%
# EDA
    # 
#%%
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
sns.set(color_codes=True)
from scipy import stats
import numpy as np
#%%
conc = pd.read_csv("Concrete_Data_Yeh.csv")

#%%
cols = list(conc.columns)
cols.pop()
#['cement', 'slag', 'flyash', 'water', 'superplasticizer', 'coarseaggregate', 'fineaggregate', 'age', 'csMPa']

#%%
conc.dtypes

#%%
conc.isnull().sum()

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
#corr = conc.iloc[:,:-1].corr() 
corr = conc.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, vmax=.3, center=0,square=True, linewidths=.5, cbar_kws={"shrink": .5})
#%%
sns.scatterplot( x=conc['age'], y=conc['csMPa'])

#%%
y=conc['csMPa']
sns.scatterplot( x=conc['cement'], y=y)

#%%
sns.scatterplot( x=conc['superplasticizer'],y=y)
#%%

sns.scatterplot( x=conc['age'],y=y, label='age')
sns.scatterplot( x=conc['cement'], y=y, label='cement')
sns.scatterplot( x=conc['superplasticizer'], y=y, label='superplasticizer')

plt.xlabel('Independent Features')
plt.title('Relationship of highly correlated features with csMPA')
fig.legend()
plt.show(fig)
#%%

