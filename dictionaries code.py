# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 16:57:28 2022

@author: aniqa
"""
import os
os.chdir(r'C:\Users\aniqa\OneDrive - The University of Texas at Dallas\Documents\GitHub\Python-Bootcamp')


fname=input("Enter file name: ")
if len(fname)<1:
    fname="clown.txt"
file=open(fname)

di=dict()
for lin in file:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds:
        di[w]= di.get(w,0) + 1

#print(di)
largest=-1

for k,v in di.items():
    print(k,v)
    if v>largest:
        largest = v
        theword=k
print(theword, largest)
    
