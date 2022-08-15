class Solution:
    def searchRange(self, nums, target: int):
        result = [-1, -1]
        ## using binary search to find start point of the target
        result[0] = self.findstartpoint(nums, target)
        ## using binary search to find end point of the target
        result[1] = self.findendpoint(nums, target)
        return result

    def findstartpoint(self, nums, target):
        result = -1

        left, right = 0, len(nums) - 1
        while left <= right:
            ## !!Best for Binary Search!!
            mid = left + int((right - left)/2)
            ## when equal target still move right cuz we want to find start point of target
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            ## when found target, update the possible index
            if nums[mid] == target:
                result = mid
        return result

    def findendpoint(self, nums, target):
        result = -1

        left, right = 0, len(nums) - 1
        while left <= right:
            ## !!Best for Binary Search!!
            mid = left + int((right - left)/2)
            ## when equal target still move left cuz we want to find end point of target
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            ## when found target, update the possible index
            if nums[mid] == target:
                result = mid
        return result

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().searchRange(arr, x))
# [1, 4]

'''
Binary Search Template:

left = 0
right = len(arr) - 1

while left <= right:
    mid = left + int((right - left)/2)
    if arr[mid] < target:
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1
    else:
        found mid = target
'''