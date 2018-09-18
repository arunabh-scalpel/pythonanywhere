#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:21:12 2018

@author: arunabhmajumdar
"""

import re
sample={}
sample["India"] = "Delhi"
sample["Pakistan"] = "Karachi"

country = input("Enter your country: ")
capital = None

if country in sample:
    print ("The capital of "+country+" is "+sample[country])