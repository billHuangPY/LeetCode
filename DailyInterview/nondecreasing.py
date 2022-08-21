'''
You are given an array of integers in an arbitrary order. 
Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

'''

def check(nums):
    mod = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            if mod:
                return False
            
            if i >= 2 and nums[i] < nums[i-2]:
                nums[i] = nums[i-1]
            mod = True
    return True

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False