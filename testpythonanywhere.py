#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:21:12 2018

@author: arunabhmajumdar
"""

import re
import pandas as pd


country = input("Enter your country: ")
country = str(country)
#capital = None
sample={}
sample["India"] = "Delhi"
sample["Pakistan"] = "Karachi"

if country in sample:
    print ("The capital of "+str(country)+" is "+str(sample[country]))
#
#print (sample)
print (sample)

