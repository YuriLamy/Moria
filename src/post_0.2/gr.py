#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['axes.grid'] = True
rcParams['axes.facecolor'] = 'orange'
rcParams['axes.labelcolor'] = 'black'
rcParams['axes.labelsize'] = 'large'
rcParams['axes.labelweight'] = 'bold'



x = np.arange(0)
y = np.arange(0)



fig = plt.figure()

ax = fig.add_subplot(111)
ax.barh(x, y)
ax.set_xlabel(u'Swing 1->2')
ax.set_ylabel(u'Swing 2->1')

ax.grid(True)

xticks = ax.get_xticks(2)
yticks = ax.get_yticks(2)

xx = np.arange(0, 10)
yy = np.arange(0, 10)

print('Xticks:', xticks)
print('Yticks:', yticks)

xlabels = []
ylabels = []
for i in xx:
    xlabels.append('%d' % i)

for j in yy:
    ylabels.append('%d' % j)
    
ax.set_xticks(xx)
ax.set_yticks(yy)
ax.set_yticklabels(['0,2', '0,15', '0,1', '0,05','0'], color='black')
ax.set_xticklabels(['0', '0,05', '0,1', '0,15', '0,2'], color='black')

yticklabels = ax.get_yticklabels()
print('Yticklabels: %s' % type(yticklabels))
print('Каждый label - это %s' % (type(yticklabels[0])))




A = [[0,0,1,2,3],[0,0,1,2,3],[0,0,1,2,2],[0,0,0,0,2], [0,0,0,0,1]]


plt.figure(1)
plt.imshow(A, cmap='BuPu', interpolation='sinc')
plt.grid(True)

#fig.suptitle('Swing', fontsize='large')

plt.show()
