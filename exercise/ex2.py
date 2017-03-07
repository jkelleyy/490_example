#!/usr/bin/python3

#Example code for problem 2 in python

import sys
from math import *;

#Returns a list of the primes dividing x along with their multiplicities
#For example factor(50)=[(2,1),(5,2)].
def factor(x):
    ret = [];
    i=2;
    while i*i<=x:
        count = 0;
        while x%i==0:
            x//=i;#note integer division
            count+=1;
        if count!=0:
            ret.append((i,count));
        i+=1;
    if x!=1:
        ret.append((x,1));
    return ret;

#This takes a list of factors and formats it using exponents and multiplication
#For example format_factors([(2,2),(3,1),(7,2)])=="2^2*3*7^2"
def format_factors(lst):
    def format_single(x):
        (p,e) = x;
        if e==1:
            return str(p);
        else:
            return str(p) + "^" + str(e);
    if len(lst)==0:
        return "1";
    else:
        return "*".join(map(format_single,lst));

line = sys.stdin.readline();
num = int(line);
print(format_factors(factor(num)));
