#!/bin/python3

#Example code for problem 1 in python

import sys

line = sys.stdin.readline();
nums = map(int,line.split());
val = 1;
for x in nums:
    val *= x;
print(val);
