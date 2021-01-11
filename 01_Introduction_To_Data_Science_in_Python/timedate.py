import pandas as pd
import numpy as np

### TIMESTAMP : specific point in time

print(pd.Timestamp('9/1/2019 10:05AM'))

print(pd.Timestamp(2019, 12, 20, 0, 0))

# isoweekday() : weekday of timestamp Monday(1) ~ Sunday(7) 
print(pd.Timestamp(2019, 12, 20, 0, 0).isoweekday())

pd.Timestamp(2019, 12, 20, 5, 2, 23).second

### PERIOD : span of time

pd.Period('1/2016')

pd.Period('3/5/2016')

print(pd.Period('1/2016') + 5)

print(pd.Period('3/5/2016') - 2)

### DATETIMEINDEX AND PERIODINDEX

t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'),
                             pd.Timestamp('2016-09-03')])
print(t1.index) # DatetimeIndex

t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'),
    pd.Period('2016-11')])

print(t2.index) # PeriodIndex


### CONVERTING TO DATETIME
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']

ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))

print(ts3)

# to_datetime()
ts3.index = pd.to_datetime(ts3.index)
print(ts3)

# to_datetime(dayfirst=True)
print(pd.to_datetime('4.7.12', dayfirst=True))

### TIMEDELTA
pd.Timestamp('9/2/2016 9:10AM') + pd.Timedelta('12D 3H')

### OFFSET
# : similar to timedelta but has certain rules.
# : allows flexibility in terms of types of time intervals.
# : business day, end of month, semi-month begin etc
pd.Timestamp('9/4/2016').weekday()

pd.Timestamp('9/4/2016') + pd.offsets.Week()

pd.Timestamp('9,4,2016') + pd.offsets.MonthEnd()


### Working with Dates in a Dataframe
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)

pd.date_range('10-01-2016', periods=9, freq='B')

pd.date_range('04-01-2016', periods=12, freq='QS-JUN') # quarter start 

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                   'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
print(df)

print(df.index.day_name())

# diff() : find difference between dates value
df.diff()

# resample()
df.resample('M').mean()
