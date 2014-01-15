#!/usr/local/bin/python3

#!/usr/bin/python
#from __future__ import division
#from __future__ import print_function

import os
import sys
import re

usage = sys.argv[0] + '\n <input> <output> \n\n'

#if len(sys.argv) != 3:
	#sys.exit(usage)

print ( 1/3, 2/5, sep=",")

'''	
input = sys.argv[1]
output = sys.argv[2]

if (not (os.path.isfile(input))):
	sys.exit( "no input\n\n")

if (os.path.isfile(output)):
	sys.exit( "output exists \n\n")

IN = open(input, "r")
#h_a = IN.readline().rstrip("\n").split("\t")

for l in IN:
	total+=1
	#l = l.rstrip("\n")
	a = l.rstrip("\n").split("\t")

#print ( "num", "\t".join(labels), sep="\t", file = OUT)


IN.close()
OUT.close
sys.exit
'''


'''
oh.write("\n")

o1 = "\t".join(["one_three",str(less)])
o2 = "\t".join(["greater_than_3",str(more)])
oh.write(o1)
oh.write("\n")
oh.write(o2)
oh.write("\n")

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

'''