# Problem Statement: Given an array of N integers, write a program to return an
# element that occurs more than N/2 times in the given array. You may consider
# that such an element always exists in the array.

def majorityElement(v: [int]) -> int:
    # Write your code here
    count, val = 1, v[0]
    for i in range(len(v)):
        if v[i] == val:
            count += 1
        else:
            count -= 1

        if count == -1:
            val = v[i]
            count = 1
    return val

print(majorityElement([1,1,1,2,3,4,4,4,4,4,4,4,4]))