'''
4 scales to know
o Ratio Scale
	- units are equally spaced
	- mathematical operations of +-/* are all valid
	- E.g. height and weight

o Interval Scale
	- units are equally spaced,
	  but there is no true zero
	- ex) degrees, compass

o Ordinal Scale:
	- the order of the units is important, but not evenly spaced.
	- Letter grades such as A+, A are a good example.

o Nominal Scale:
	- categories of data, but the
	  categories have no order with respect to one another.
	- teams of a sport
'''
import pandas as pd
df=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
		index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good',
                    'ok', 'ok', 'ok', 'poor', 'poor'],
                columns=['Grades'])

# above is currently an object type.
# we can change using astype
df['Grades'].astype('category')

# or we could assign custom category order
my_categories = pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-',
'A', 'A+'], ordered=True)
grades = df['Grades'].astype(my_categories)

# we can see the difference 
df[df['Grades']>'C']
# gives wrong answer while,
grades[grades>'C']
# is correct

# cut()
import numpy as np
df = pd.read_csv('datasets/census.csv')
df = df[df['SUMLEV']==50]

df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(np.average)
pd.cut(df, 10)
