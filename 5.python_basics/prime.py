from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input(""))
if(n==1): 
    print("NO")
    quit()
for i in range(2,int(sqrt(n))+1):
    if n % i==0:
        print("NO")
        quit()
print("YES")