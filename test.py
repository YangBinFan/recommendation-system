# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:28:49 2022

@author: Yang-Bin Fan
"""

import os
import json

one_path = "./data/test.txt"

# a = os.path.exists(path)

# b = json.load(open("./data/test.txt"))

with open(one_path,"r") as fp:
    for line in fp.readlines():
        if line.strip().endswith(":"):
            continue
        userID , _ , _ =line.split(",")