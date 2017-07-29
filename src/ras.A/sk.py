#!/usr/bin/python

# -*- coding: utf-8 -*-
if __name__ == "__main__":
    print sys.argv
    print("\n\n Starting tree processing\n\n")

f=open('res','a')
line = f.readline()
while line:
    print (line),
    line = f.readline()
    outs = process()
    f.write('{0}\t{1}'.format(sys.argv[1], outs))
    f.close()
