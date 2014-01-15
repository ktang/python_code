#!/usr/local/bin/python3


#!/usr/bin/python
#from __future__ import division
#from __future__ import print_function
#from __future__ import print_function

import sys
import re
import os



usage = sys.argv[0] + '\n <input> <output> \n\n'

if len(sys.argv) != 3:
	sys.exit(usage)
	
input = sys.argv[1]
output = sys.argv[2]

if (not (os.path.isfile(input))):
	sys.exit( "no input\n\n")

if (os.path.isfile(output)):
	sys.exit( "output exists \n\n")

IN = open(input, "r")
h_a = IN.readline().rstrip("\n").split("\t")

print (len(h_a) )
labels = []
indexs = []


#print h_a.
for i in range( len(h_a) ):
	#print (i, h_a[i] ,sep='\t')
	if ( re.search( r'overlap_(\S+)' , h_a[i]) ):
		m = re.search('^overlap_(\S+)', h_a[i])
		#print (i, m.group(1),sep="\t")
		labels.append(m.group(1))
		indexs.append(i)
#print (labels)
#print (indexs)

#print(*objects, sep=' ', end='\n', file=sys.stdout)
#print head
#, "\n"
#sys.exit

OUT = open(output, "w")
total = 0
nums = {}#AutoVivification()

for l in IN:
	total+=1
	#l = l.rstrip("\n")
	a = l.rstrip("\n").split("\t")
	flags = []
	for i in (range(len(indexs))):
		if( a[indexs[i]] == "NOT"):
			flags.append("Not")
		else:
			flags.append("Overlap")
	
	flag = '\t'.join(flags)
	#nums[flag]+=1
#'''
	if not flag in nums:
		nums[flag] = 1
	else: nums[flag]+=1
#'''

IN.close()

sum = 0

print ( "num", "\t".join(labels), sep="\t", file = OUT)

for k in sorted(nums.keys()):
	sum+= nums[k]
	#print (nums[k], k.split("_"), sep="\t", file=OUT)
	print (nums[k], k, sep="\t", file=OUT)

if(sum != total):
	print ("NOT equal\n\n")

OUT.close
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