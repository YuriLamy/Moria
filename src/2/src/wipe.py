#!/usr/bin/python

import os
import sys

if len(sys.argv)<2:
    rt = 'archive'
else:
    rt = sys.argv[1]
cmd = "tar czf %s.tar.gz tree*.tre params.ctl envi.ctl envi1.ctl swing.ctl" %sys.argv[1]
os.system(cmd)
os.system("rm -f tree*.tre")
print "i ququ"
