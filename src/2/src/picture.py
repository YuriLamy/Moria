#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np
import pylab as P

fname = "res"

tabl=np.loadtxt(fname)
n,bins,patches = P.histogram(tabl[:,0], 10, normed=1, histtype='stepfilled')
l = P.plot(bins, y, 'k--', linewidth=1.5)
