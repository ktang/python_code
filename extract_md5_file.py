#!/usr/local/bin/python3

#!/usr/bin/python
#from __future__ import division
#from __future__ import print_function
#from __future__ import print_function

import sys
import re
import os

debug = 1

usage = sys.argv[0] + '\n <input>  \n\n'

if len(sys.argv) != 2:
	sys.exit(usage)
	
input = sys.argv[1]
#output = sys.argv[2]

if (not (os.path.isfile(input))):
	sys.exit( "no input\n\n")

IN = open(input, "r")

'''
for i in range( len(h_a) ):
	#print (i, h_a[i] ,sep='\t')
	if ( re.search( r'overlap_(\S+)' , h_a[i]) ):
		m = re.search('^overlap_(\S+)', h_a[i])
		#print (i, m.group(1),sep="\t")
		labels.append(m.group(1))
		indexs.append(i)
'''
nums = {}#AutoVivification()

for l in IN:
	#a = l.rstrip("\n").split("\t")
	l = l.rstrip("\n")
	if (re.search(r'^MD5',l)):
		if(debug): print("Here", file = sys.stderr )
		m = re.search(r'\((\S+)\)\s*=\s*(\S+)', l)
		#if(debug): print ( m.group(1), m.group(2),  sep="\t" )
		nums[ m.group(1)] = m.group(2)

#if(debug):sys.exit
#print ( "num", "\t".join(labels), sep="\t", file = OUT)

for k in sorted(nums.keys()):
	#sum+= nums[k]
	#print (nums[k], k.split("_"), sep="\t", file=OUT)
	print (k, nums[k], sep="\t")

#if(sum != total):
#	print ("NOT equal\n\n")

#OUT.close
sys.exit



'''
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
oh.write(file)
oh.write("\n")

o1 = "\t".join(["one_three",str(less)])
o2 = "\t".join(["greater_than_3",str(more)])
oh.write(o1)
oh.write("\n")
oh.write(o2)
oh.write("\n")
'''