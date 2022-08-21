def singleNumber(nums):
    ## the solution is to xor every number in the list and get the result, curr is 
    ## the current result of xor'ed numbers, initialized with first number is list
    curr = nums[0]
    ## iterate all remain numbers and xor all of them
    for i in range(1, len(nums)):
        curr = curr ^ nums[i]
    ## return the xor result of all numbers
    return curr

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1