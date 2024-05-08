def search(nums: [int], target: int):
    left = 0
    right = len(nums)-1
    mid = (left + right)/2
    while left<=right:
        if a[mid]==target: return 1
        elif a[mid]<target: return left =mid+1
        else: right=mid-1
    
    return -1
