# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 23:30:14 2021

@author: seung
"""


Man1 = input("Man1 : ")
Man2 = input("Man2 : ")

RSP = ["가위", "바위", "보"]

if Man1 == Man2:
    print("Result : Draw")
elif Man1 == RSP[1] and Man2 == RSP[0]:
    print("Result : Man1 Win!")
elif Man1 == RSP[2] and Man2 == RSP[1]:
    print("Result : Man1 Win!")
elif Man1 == RSP[0] and Man2 == RSP[2]:
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")
