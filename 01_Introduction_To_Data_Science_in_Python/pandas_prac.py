import pandas as pd
import numpy as np

students = ['Alice', 'Jack', 'Molly']

pd_students = pd.Series(students)
# pandas automatically assigns indices

print(pd_students)

numbers = [1,2,3]
print(pd.Series(numbers))

# What about None data?
students = ['Alice', 'Jack', None]
print(pd.Series(students))

numbers = [1,2,None]
print(pd.Series(numbers))
# NOTE that NaN is considered as float type

# NOTE np.nan != None
print(np.nan == None)
print(np.nan == np.nan)
# We can test if nan by isnan()
print(np.isnan(np.nan))

s = pd.Series(['Physics', 'Chemistry', 'English'], index=['Alice', 'Jack','Molly'])
print(s)

### Querying Series

# Use iloc to query by index
# Use loc to query by label
students_classes = {'Alice': 'Physics',
                    'Jack': 'Chemistry',
                    'Molly': 'English',
                    'Sam':'History'}
s = pd.Series(students_classes)
print(s)

print('iloc:', s.iloc[3])
print('loc:', s.loc['Molly'])
# NOTE iloc and loc can be usually implied. But take care where keys are numbers

class_code = {99: 'Physics',
        100:'Chemistry',
        101:'English',
        102:'History'}
s = pd.Series(class_code)
print(s.iloc[3])

# Pandas can be used with numpy
grades = pd.Series([90, 80, 70, 60])
total = 0
for grade in grades:
    total += grade
print(total/len(grades))


total = np.sum(grades)
print(total/len(grades))

# Is this really faster?
numbers = pd.Series(np.random.randint(0, 1000, 10000))
print(numbers.head())

# Broadcasting is also possible like numpy
numbers += 2
print(numbers.head())

for label, value in numbers.iteritems():
    #print('label:', label, 'value:', value)
    numbers.loc[label] = value+2
print(numbers.head())

# loc can also add new values if they do not exist
s = pd.Series([1,2,3])
s.loc['History'] = 102
print(s)

# Pandas allows non unique index values
students_classes = pd.Series({'Alice': 'Physics',
    'Jack': 'Chemistry',
    'Molly': 'English',
    'Sam':'Histroy'})

kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Kelly', 'Kelly', 'Kelly'])
print(kelly_classes)

all_students_classes = students_classes.append(kelly_classes)
print(all_students_classes)

# Pandas, by default, returns a new object, rather than manipulating original object

print(students_classes)
