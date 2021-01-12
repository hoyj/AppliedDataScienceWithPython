import numpy as np
import pandas as pd
from scipy import stats

# When we do hypothesis testing, we actually have two statements of interest: 
# the first is our actual explanation, which we call the alternative hypothesis,
# and the second is that the explanation we have is not sufficient, and we call this
# the null hypothesis. Our actual testing method is to determine wheter the null hypothesis is true
# or not.

df = pd.read_csv('datasets/grades.csv')
print(df.head())

early_finishers = df[pd.to_datetime(df['assignment1_submission']) < '2016']
print(early_finishers.head())

#late_finishers = df[pd.to_datetime(df['assignment1_submission']) >= '2016']
late_finishers = df[~df.index.isin(early_finishers.index)]


print(early_finishers['assignment1_grade'].mean())
print(late_finishers['assignment1_grade'].mean())

# They look similar. But, are they the same? What do we mean by similar? This is where 
# the students' t-test come in. It allows us to form the alternative hypothesis 
# ("These are different") as well as the null hypothesis ("These are the same") and 
# test that null hypothesis

# When doing hypothesis testing, we have to choose a significance level as a threshold
# for how much of a chance we're willing to accept. This significance level is typically
# called alpha.

# ttest_ind() : does an independent t-test(not related to one another).
#               returns t-statistic and a p-value.
from scipy.stats import ttest_ind
print(ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignment1_grade']))

'''
P-values have come under fire recently for being insufficient for telling us enough about hte
interactions which are happening, and two other techniques, confidence intervalues and bayesian
analysis, are being used more regularly. One issue with p-values is that as you run more tests, you
are likely to get a value which is statistically significant just by chance.
'''

# for example
df1 = pd.DataFrame([np.random.random(100) for x in range(100)])
print(df1.head())

df2 = pd.DataFrame([np.random.random(100) for x in range(100)])
print(df2.head())

# are these two df the same? For a given row inside of df1, is it the same as the row inside df2?

# Lets take a look, let's say our critical value is 0.1, or and alpha of 10%. And we're going to
# compare each column in df1 to the same numbered column in df2. And we'll report when the p-value
# isn't less than 10%, which means that we have sufficient evidence to say that the columns are
# different.

def test_columns(alpha=0.1):
    num_diff = 0
    for col in df1.columns:
        teststat, pval = ttest_ind(df1[col], df2[col])
        if pval <= alpha:
            print('Col {} is statistically significantly different at alpha={}, \
                pval={}'.format(col, alpha, pval))
            num_diff = num_diff + 1
    print('Total number different was {}, which is {}%'.format(num_diff,
        float(num_diff)/len(df1.columns)*100))
test_columns()

test_columns(0.05)

df2=pd.DataFrame([np.random.chisquare(df=1, size=100) for x in range(100)])


