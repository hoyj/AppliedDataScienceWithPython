import matplotlib.pyplot as plt
import numpy as np
# scatter plots

x = np.array(range(1,9))
y = x
colors = ['green'] * (len(x)-1)
colors.append('red')

plt.figure() # create figure()
plt.scatter(x, y, s=100, c=colors)

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
print(list(zip_generator))

plt.figure()
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')

plt.xlabel('The number of times the child kicked aball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')

plt.legend(loc=4, frameon=False, title='Legend')

print(plt.gca().get_children())
legend = plt.gca().get_children()[-2]

from matplotlib.artist import Artist

def rec_gc(art, depth=0):
    if isinstance(art, Artist):
        print(' ' *depth + str(art))
        for child in art.get_children():
            rec_gc(child, depth+2)
rec_gc(legend)

### line plots
linear_data = np.array(range(1,9))
quadratic_data =linear_data **2

plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')
plt.plot([22,44,55], '--r')
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline', 'Competition', 'Us'])

plt.gca().fill_between(range(len(linear_data)),
                        linear_data, quadratic_data,
                        facecolor='blue',
                        alpha=0.25)

plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
plt.plot(observation_dates, linear_data, '-o',
        observation_dates, quadratic_data, '-o')

x = plt.gca().xaxis

for item in x.get_ticklabels():
    item.set_rotation(45)

plt.subplots_adjust(bottom=0.25)

ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Quadratic vs. Linear performance')

ax.set_title('Quadratic ($x^2$) vs. Linear($x$) performance') # latex

### Bar charts
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3)

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, quadratic_data, width=0.3, color='red')

from random import randint
linear_err = [randint(0, 15) for x in range(len(linear_data))]
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3, color='b')
plt.bar(xvals, quadratic_data, width=0.3, bottom=linear_data, color='r')

plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height=0.3, color='b')
plt.barh(xvals, quadratic_data, height=0.3, left=linear_data, color='r')


### dejunkifying a plot
# removing ticks
plt.tick_params(top='off', bottom='off', left='off', right='off', labelbottom='off',
        labelleft='off')

# removing frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# soften labels by turning grey
plt.bar(..., color='lightslategrey')
bars[0].set_color('#1F77B4')
plt.xticsk(..., alpha=0.8)

# remove y labels
#plt.ylable(...)
# and direct label each bar with Y axis values
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height()) + '%', 
        ha='center', color='w', fontsize=11)

plt.show()
