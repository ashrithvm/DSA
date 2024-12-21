given_arr = [8,6,3,5,4,1,2]

def merge_sort(arr):
    length = len(arr)
    if length <=1: return

    mid = length//2
    left, right = arr[:mid], arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

def merge(left, right, arr):
    left_size = len(left)
    right_size = len(right)
    i, l, r = 0,0,0
    while l < left_size and r < right_size:
        if left[l] < right[r]:
            arr[i] = left[l]
            l+=1
            i+=1
        else:
            arr[i] = right[r]
            r+=1
            i+=1
    while r < right_size:
        arr[i]=right[r]
        i+=1
        r+=1
    while l < left_size:
        arr[i] = left[l]
        i+=1
        l+=1

merge_sort(given_arr)
print(given_arr)

