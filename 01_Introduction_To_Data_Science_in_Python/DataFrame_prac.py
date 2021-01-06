import pandas as pd

# A dataframe is the core of pandas. It is different from Series in that Series
# can only have single list/

record1 = pd.Series({'Name': 'Alice',
                    'Class':'Physics',
                    'Score':85})
record2 = pd.Series({'Name': 'Jack',
                    'Class':'Chemistry',
                    'Score':82})
record3 = pd.Series({'Name': 'Helen',
                    'Class':'Biology',
                    'Score':90})

df = pd.DataFrame([record1, record2, record3],
        index=['school1', 'school2', 'school1'])

print(df.head())
# Above can be a list passed into a DataFrame

# We can also use .iloc and .loc # returns Series
print(df.loc['school2'])

# Could also use non-unique labels # this returns DataFrame
print(df.loc['school1'])

# NOTE iloc and loc are used for row selection
print(df['Name'])
#print(df.loc['Name']) # << Will produce error because not a row

# drop(inplace=False,axis=0) - to remove row. axis=1 to remove col


### DataFrame indexing and Loading

# read_csv() : read in csv files
df = pd.read_csv('datasets/Admissions_Predict.csv')
print(df)

# index_col=0 to set which column as index
df = pd.read_csv('datasets/Admissions_Predict.csv', index_col=0)
print(df)

# rename() : to modify column names
new_df = df.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score',
    'University Rating': 'University Rating',
    'SOP': 'Statement of Purpose', 'LOR': 'Letter of Recommendation',
    'CGPA':'CGPA', 'Research': 'Research', 'Chance of Admit': 'Chance of Admit'})
print(new_df.head())


# rename(mapper=FUNCTION, axis='columns') : to map given function on axis
new_df = df.rename(mapper=str.strip, axis='columns')

# .columns : we can use .columns attribute to find column names
# Also, note that rename() does not change the acutal DataFrame.
# using .columns can actually modify the DataFrame

cols = list(df.columns)
print(cols)
cols = [x.lower().strip() for x in cols]
df.columns = cols

### DataFrame Querying
df = pd.read_csv('datasets/Admissions_Predict.csv', index_col=0)
df.columns = [x.lower().strip() for x in df.columns]
print(df.head())

admit_mask = df['chance of admit'] > 0.7 # returns Series
print(admit_mask)

# where() : to only show data which corresponds to condition
print(df.where(admit_mask).head()) # Hidden data are shown as NaN
# we can use .dropna() to not show NaN
print(df.where(admit_mask).dropna().head())
# Just like numpy
print(df[df['chance of admit'] > 0.7].head())

# NOTE and , or cannot be used in pandas. Use &,| instead
# In this case, must use with (, ).
print(df['chance of admit'].lt(0.9).gt(0.7))

### Indexing DataFrames
df = pd.read_csv('datasets/Admissions_Predict.csv', index_col=0)
print(df.head())

# set_index() : set new column as index. But we can always keep original serial number,
#               by savining into another column by calling .index

df['Serial Number'] = df.index
df = df.set_index('Chance of Admit ')
print(df.head())

# reset_index() : can be used to promote current index into a column and creates a default index
df = df.reset_index()
print(df.head())

# Pandas allows mult-level indexing
df = pd.read_csv('datasets/census.csv')
print(df.head())

# .unique() : to see unique values
print(df['SUMLEV'].unique())

df = df[df['SUMLEV'] == 50]
print(df.head())

columns_to_keep = ['STNAME', 'CTYNAME', 'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013',
'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',
'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']

df = df[columns_to_keep]
df.head()

# multi index : use set_index with [] to apply multi indexing
df = df.set_index(['STNAME', 'CTYNAME'])
print(df.head())

# NOTE: When querying a multi indexed data using loc, must be ordered by level.
print(df.loc['Michigan', 'Washtenaw County'])

# If we want to compare, then use tuples
print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])

### MISSING VALUES : Missing values could be important information
df = pd.read_csv('datasets/class_grades.csv')
print(df.head(10))

# isnull() : create a bool mask of DataFrame
mask = df.isnull()
print(mask.head(10))
print(df.dropna().head(10))

# fillna() : fill with number. inplace optional
df.fillna(0, inplace=True)
print(df.head(10))

df = pd.read_csv('datasets/log.csv')
print(df.head())

# parameter() : ffill - fill with recent valid value, bfill - fill with next valid value
df = df.set_index('time')
df = df.sort_index()
print(df.head())

df = df.reset_index()
df = df.set_index(['time', 'user'])
print(df.head())

df = df.fillna(method='ffill')
print(df.head())

# replace() : can replace with value
# we can also use regex with regex=True as 3rd parameter
