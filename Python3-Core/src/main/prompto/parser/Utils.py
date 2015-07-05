'''
Created on 24 fevr. 2014

@author: ericvergnaud
'''

import inspect
import string

def extractTokenNames(lexerType):
    mod = inspect.getmodule(lexerType)
    mbs = inspect.getmembers(mod)
    names = [None] * len(mbs)
    for mb in mbs:
        if isinstance(mb[1],int) and mb[1]<len(names) and str(mb[0]).upper()==mb[0]:
            names[mb[1]] = mb[0]
    return names
    
    