# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:11:22 2020

@author: Nandy
"""

def ErrorModel(m,b,data):
    """
    f:x|--> mx+b
    data = {(x,y)}
    """
    n = len(data)
    return (1/n) *sum(((m*data[i][0]+b) - data[i][1] for i in range(n))^2)



