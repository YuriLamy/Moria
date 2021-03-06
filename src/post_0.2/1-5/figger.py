#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
рисовалка для mlya
'''
import sys
import numpy as np 
import matplotlib.pyplot as plt
fig = plt.figure()

ax = fig.add_subplot(111)
 
ax.set_xlabel(u'Количество репродуктивных циклов')
ax.set_ylabel(u'Численность популяции')

dta = np.loadtxt("demogr.dat",delimiter="\t")
dta1 = np.array(dta)
x=dta1[:,0]
y1=dta1[:,1]
y2=dta1[:,2]
y3=dta1[:,3]
y4=dta1[:,4]
plt.plot(x, y1, 'r-')
plt.plot(x,y2,'r.')
plt.plot(x, y3, 'b-')
plt.plot(x,y4,'b.')

#fig.suptitle('График заданных условий')

plt.show()
