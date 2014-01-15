#!/usr/bin/python

import sys
import re

usage = "sys.argv[0] input";


if len(sys.argv) != 2:
	sys.exit(usage)
file = sys.argv[1];
match = re.search('(\S+).soap$',file)
if match:
	pre = match.group(1)
out = pre + "_profile.txt";
oh = open (out, "w")
more = 0
less = 0

#fh = open (file, "r")
myfile = "./" + file;

last = "NULL"
#whlie line = fh.readline():

for line in open(myfile,'r'):
	line.rstrip()
	pts = line.split("\t")
	if pts[0] != last:
		last = pts[0]
		if int(pts[3]) <= 3:
			less += 1
		elif int(pts[3]) > 3:
#			print pts[3]
			more += 1
		else:
			sys.exit("wrong number")
	else: pass

oh.write(file)
oh.write("\n")

o1 = "\t".join(["one_three",str(less)])
o2 = "\t".join(["greater_than_3",str(more)])
oh.write(o1)
oh.write("\n")
oh.write(o2)
oh.write("\n")