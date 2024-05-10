def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    akk=[]
    l=len(arr)
    for i in range(0,l):
        new_index=(i+k)%l
        akk.append(arr[new_index])
    arr=akk
    return arr
