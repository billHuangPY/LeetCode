def sortNums(nums):
    left, ptr, right = 0, 0, len(nums)-1
    while ptr <= right:
        ## if current pointer has "1" then swap it with the leftmost pointer, and move the left and index pointer to next one
        if nums[ptr] == 1:
            nums[left], nums[ptr] = nums[ptr], nums[left]
            left += 1
            ptr += 1
        ## if current pointer has "2" then move pointer to next, keep finding 1 or 3 to swap
        elif nums[ptr] == 2:
            ptr += 1
        ## if current pointer has "3" then swap it with the rightmost pointer, and more back the rightmost pointer
        elif nums[ptr] == 3:
            nums[right], nums[ptr] = nums[ptr], nums[right]
            right -= 1
            
    return nums

print(sortNums([3,1,2,1,3,2,3,1,2,3,1,2,3,2,2,3,3,3,1,2,3,1,2,3,1]))
# [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
