## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n = int(input(''))
e=0
o=0
while(n!=0):
    d=n%10
    n=n//10
    if(d%2==0):
        e=e+d
    else:
        o=o+d
print(f"{e} {o}")