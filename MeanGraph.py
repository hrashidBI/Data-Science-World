""" import numpy as np
import matplotlib.pyplot as plt

# two different arrays
x = np.array([2,3,5,6])
y = np.array([-8,-7,15,16])

# needed for the graph below
my_range = np.arange(4)

# their respective means
mean_x = np.mean(x)
mean_y = np.mean(y)

fig, axs = plt.subplots(1,2, sharey=True)
axs[0].stem(my_range, x, label='x values', bottom=mean_x) 
axs[1].stem(my_range, y, label='y values', bottom=mean_y)
legend_x = axs[0].legend(loc='upper right')
legend_y = axs[1].legend(loc='lower right')
plt.show() """


import matplotlib.pyplot as plt
import numpy as np

#define data
x = [1, 2, 3, 4, 5, 6]
y = [3, 7, 14, 19, 15, 11]

my_range = np.arange(4)
#create line plot
plt.plot(x, y)

mean_x = np.mean(x)
mean_y = np.mean(y)

#plt.plot(y)

fig, axs = plt.subplots(1,2, sharey=True)
axs[0].stem(my_range, x, label='x values', bottom=mean_x) 
axs[1].stem(my_range, y, label='y values', bottom=mean_y)
legend_x = axs[0].legend(loc='upper right')
legend_y = axs[1].legend(loc='lower right')

#show line plot
plt.show()