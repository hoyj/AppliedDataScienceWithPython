import pandas as pd
import numpy as np

'''
pivot tables : a way of summarizing data in a DF for a particular purpose.
               to see the relationship between variables
'''

df = pd.read_csv('datasets/cwurData.csv')
print(df.head())

def create_category(ranking):
    if (ranking >= 1) & (ranking <= 100):
        return 'First Tier Top University'
    elif (ranking >= 101) & (ranking <= 200):
        return 'Second Tier Top University'
    elif (ranking >= 201) & (ranking <= 300):
        return 'Third Tier Top University'
    return 'Other Top University'

df['Rank_Level'] = df['world_rank'].apply(lambda x: create_category(x))
print(df.head())

print(df.pivot_table(values='score', index='country', columns='Rank_Level',
    aggfunc=[np.mean]).head())

print(df.pivot_table(values='score', index='country', columns='Rank_Level',
    aggfunc=[np.mean, np.max]).head())

new_df = df.pivot_table(values='score', index='country', columns='Rank_Level',
    aggfunc=[np.mean, np.max], margins=True)

print(new_df.index)
print(new_df.columns)

print(new_df['mean']['First Tier Top University'].head()) # Series

# idxmax() : Series built in function. Similar to numpy argmax
print(new_df['mean']['First Tier Top University'].idxmax()) 

# Stack, unstack
new_df = new_df.stack()
print(new_df.head())

print(new_df.unstack().unstack().head())
