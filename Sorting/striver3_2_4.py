# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.
#

def maxSubarraySum(arr):
    n = len(arr)
    if n==0:
        return 0
    if n==1:
        return max(0,arr[0])

    high, curr = arr[0], arr[0]

    for i in range(1,n):
        curr+=arr[i]
        if curr<0:
            curr=0
        high = max(high, curr)

    return high

print(maxSubarraySum([1, 2, 7, -4, 3, 2, -10, 9, 1]))