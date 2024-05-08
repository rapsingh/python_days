from os import *
from sys import *
from collections import *
from math import *

def selectionSort(arr,n):
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if(arr[min_idx]>arr[j]):
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

