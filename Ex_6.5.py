# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 23:47:31 2022

@author: aniqa
"""


str = 'X-DSPAM-Confidence:0.8475'

x=str.find(":")
print(x)
print(str[x+1:])
y=float(str[x+1:])
print(type(y))