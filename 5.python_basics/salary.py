from os import *
from sys import *
from collections import *
from math import *

def custom_round(number):
    integer_part = int(number)
    decimal_part = number - integer_part
    if decimal_part >= 0.5:
        return int(integer_part+1)
    else:
        return integer_part

def totalSalary(basic, grade):
	hra=0.2*basic
	da=0.5*basic
	allowance=0
	pf=0.11*basic
	if(grade=='A'):allowance=1700
	elif(grade=='B'):allowance=1500
	else:allowance=1300
	tot_salary=allowance+1.59*basic
	return int(custom_round(tot_salary))