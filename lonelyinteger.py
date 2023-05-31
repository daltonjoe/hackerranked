import math
import os
import random
import re
import sys


def lonelyinteger(a):
    temp=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j]:
                temp.append(a[i])
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1

    for num in a:
        if freq[num] == 1:
            print(num)   

# def lonelyinteger(a):
#     for num in a:
#         if a.count(num) == 1:
#             return num            


a=[1,1,2,3,3]
result = lonelyinteger(a)
print(result)

    
