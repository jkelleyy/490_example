#!/usr/bin/python3

#Example code for problem 4 in python

import sys

#represents an element of the disjoint set data structure
class DJSElem:
    def __init__(self,x):
        self.parent = x;
        self.rank = 0;

#The disjoint set data structure representing a disjoint collection of subsets of 1,...,n
class DJS:
    def __init__(self,n):
        self.data = list(map(lambda x : DJSElem(x),range(0,n)));
        self.nSubsets = n;
    #finds a representative for the set that x belongs to.
    #The idea is that if x,y are in the same subset if and only if find(x)=find(y)
    def find(self,x):
        if x!=self.data[x].parent:
            self.data[x].parent = self.find(self.data[x].parent);
        return self.data[x].parent
    #like find by return a DJSElem instead of an integer
    def findElem(self,x):
        return self.data[self.find(x)]
    #take the union of the sets containing a and b
    def union(self,a,b):
        ap = self.findElem(a);
        bp = self.findElem(b);
        if ap != bp:
            self.nSubsets -= 1;
            if ap.rank<bp.rank:
                ap.parent = bp.parent;
            elif ap.rank>bp.rank:
                bp.parent = ap.parent;
            else:
                ap.parent = bp.parent;
                bp.rank += 1;


line = sys.stdin.readline();
n,e = map(int,line.split());
djs = DJS(n);
for i in range(0,e):
    line = sys.stdin.readline();
    a,b = map(int,line.split());
    djs.union(a,b)
print(djs.nSubsets)
