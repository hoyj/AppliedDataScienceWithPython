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
