def sort_colors(nums):

    def swap(a, b):
        nums[a], nums[b] = nums[b], nums[a]

    low, mid, high = 0, 0, len(nums)-1

    while mid<=high:
        if nums[mid]==0:
            swap(low, mid)
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            swap(mid, high)
            high-=1

nums = [2,0,2,1,1,0]
sort_colors(nums)
print(nums)