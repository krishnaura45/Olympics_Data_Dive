# -*- coding: utf-8 -*-
## Getting Started
"""

import numpy as np
import pandas as pd

"""**Loading the csv files**"""

df=pd.read_csv('/content/all_athlete_games.csv')
region_df=pd.read_csv('/content/all_regions.csv')

df.sample(10)

df.shape

region_df.tail()

region_df.shape

"""**Merging files on the basis of NOC**"""

df= df.merge(region_df,on='NOC',how='left')

df.head()

"""## Working on Summer Olympics Data

**Extraction of Summer Olympics data**
"""

dfs= df[df['Season']=='Summer']
dfs.shape

dfs.tail()

# countries participated
dfs['Region'].unique()

# number of countries particicpated
dfs['Region'].unique().shape

# missing values
dfs.isnull().sum()

# duplicate rows
dfs.duplicated().sum()

# number of different categories of medals
dfs['Medal'].value_counts()

# one hot encoding
pd.get_dummies(dfs['Medal'])

dfs=pd.concat([dfs,pd.get_dummies(dfs['Medal'])],axis=1)
dfs.sample(5)

dfs.shape

tally1=dfs.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
tally1.head(25)

"""Tally1: Wrong Tally of Medals"""

# Why?
dfs[(dfs['NOC']=='IND') & (dfs['Medal']=='Gold')]

"""We need to duplicate rows so as to correct medal tally"""

dfs=dfs.drop_duplicates(subset=['Team','NOC','Year','City','Sport','Event','Medal'])

tally2=dfs.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
tally2

"""Tally 2: Almost Correct Tally"""

tally2[tally2['NOC']=='IND']

"""Now, we have got correct tally of medals for INDIA as mentioned at <a href="https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table" target="_blank">WIKI</a>"""

years = dfs['Year'].unique().tolist()
years

years.sort()
years.insert(0,'Overall')
years

country = np.unique(dfs['Region'].dropna().values).tolist()
country

country.sort()
country.insert(0, 'Overall')
country

nations_over_time = dfs.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('index')
nations_over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)
