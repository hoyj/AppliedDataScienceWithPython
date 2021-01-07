import pandas as pd

### Outer/Inner joins 

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liaison'},
                         {'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

print(staff_df.head())
print(student_df.head())

print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))
print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))

### Left/Right join
print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))
print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

# on keyword
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

print(pd.merge(staff_df, student_df, how='right', on='Name'))

# What if we have conflicts? ==> _x (for left), _y (for right)
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR',
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liaison',
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader',
                          'Location': 'Washington Avenue'}])

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business',
                            'Location': '1024 Billiard Avenue'},
                            {'Name': 'Mike', 'School': 'Law',
                             'Location': 'Fraternity House #22'},
                            {'Name': 'Sally', 'School': 'Engineering',
                             'Location': '512 Wilson Crescent'}])
print(pd.merge(staff_df, student_df, how='left', on='Name'))

# What if they overlap for single column but are actually different? ==> multi indexing
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins',
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks',
                          'Role': 'Course liaison'},
                         {'First Name': 'James', 'Last Name': 'Wilde',
                          'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond',
                          'School': 'Business'},
                         {'First Name': 'Mike', 'Last Name': 'Smith',
                          'School': 'Law'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks',
                          'School': 'Engineering'}])

print(pd.merge(staff_df, student_df, how='inner', on=['First Name', 'Last Name']))


### IF merge == 'horizontal', then concatenating is 'vertical'
# assuming they all have same columns
#frames = [df_2011, df_2012, df_2013]
#pd.concat(frames)

# to distinguish which data each is from, we can use keys keyword.
#pd.concat(frames, keys=['2011', '2012', '2013'])


### Pandas idioms
import pandas as pd
import numpy as np
import timeit

df = pd.read_csv('datasets/census.csv')
print(df.head())

# method chaining
print((df.where(df['SUMLEV']==50)
        .dropna()
        .set_index(['STNAME', 'CTYNAME'])
        .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})))
print(df.where(df['SUMLEV']==50))

def first_approach():
    global df
    return (df.where(df['SUMLEV']==50)
                .dropna()
                .set_index(['STNAME', 'CTYNAME'])
                .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

df = pd.read_csv('datasets/census.csv')
print(timeit.timeit(first_approach, number=10))

def second_approach():
    global df
    new_df = df[df['SUMLEV']==50]
    new_df.set_index(['STNAME', 'CTYNAME'], inplace=True)
    return new_df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})


df = pd.read_csv('datasets/census.csv')

print(timeit.timeit(second_approach, number=10))

# applymap : map on all cells
# apply : map on rows
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

print(df.apply(min_max, axis='columns').head())

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]

    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row

print(df.apply(min_max, axis='columns').head())

# apply is usually used with lambdas
rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013','POPESTIMATE2014', 'POPESTIMATE2015']
print(df.apply(lambda x: np.max(x[rows]), axis=1).head())

# group by
df = pd.read_csv('datasets/census.csv')
df = df[df['SUMLEV']==50]
print(df.head())

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state +
          ' have an average population of ' + str(avg))

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])

df = df.set_index('STNAME')

def set_batch_number(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

df = pd.read_csv('datasets/listings.csv')
df.head()
# could use multi index and groupby()
df = df.set_index(['cancellation_policy', 'review_scores_value'])

for group, frame in df.groupby(level=(0,1)):
    print(group)

def grouping_fun(item):
    if item[1] == 10.0:
        return (item[0],"10.0")
    else:
        return (item[0],'not 10.0')

for group, frame in df.groupby(by=grouping_fun):
    print(group)

# Pandas developers have three broad categories of data processing during apply step.
# Aggregation of group data, Transformation, and Filtration

### AGGREGATION

# agg() # using dictioanries in agg() may be deprecated
# one row per group
df = df.reset_index()
df.groupby("cancellation_policy").agg({"review_scores_value": np.nanmean})
df.groupby("cancellation_policy").agg({"review_scores_value": (np.nanmean, np.nanstd),
                                       "reviews_per_month":np.nanmean})

### TRANSFORMATION
# : is differnet from aggregation
# agg() returns a single value per column.
# transform() returns object that is same size as group.

cols = ['cancellation_policy', 'review_scores_value']
transform_df=df[cols].groupby('cancellation_policy').transform(np.nanmean)
transform_df.head()
transform_df.rename({'review_scores_values': 'mean_review_scores'}, axis='columns', inplace=True)
df=df.merge(transform_df, left_index=True, right_index=True)

df['mean_diff'] = np.absolute(df['review_scores_value']-df['mean_review_scores'])

### FILTERING
df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.2)


### APPLYING
df = pd.read_csv('datasets/listings.csv')
df=df[['cancellation_policy', 'review_scores_value']]

def calc_mean_review_scores(group):
    avg = np.nanmean(group['review_scores_value'])
    group['review_scores_mean'] = np.abs(avg-group['review_scores_value'])
    return group

df.groupby('cancellation_policy').apply(calc_mean_review_scores).head()
