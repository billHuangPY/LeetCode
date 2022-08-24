'''
Given a list of numbers, find if there exists a pythagorean triplet 
in that list. A pythagorean triplet is 3 variables a, b, c 
where a**2 + b**2 = c**2

Input: [3, 5, 12, 5, 13]
Output: True
Here, 5**2 + 12**2 = 13**2.
'''


'''
Time: O(n**2)
Space: O(n)
'''

def findPythagoreanTriplets(nums):
    mp = {}
    sqnums = []
    for num in nums:
        square = num**2
        if not square in mp:
            mp[square] = True
            sqnums.append(square)

    for left in range(len(sqnums)-1):
        numleft = sqnums[left]
        for right in range(left+1,len(sqnums)):
            nsum = numleft + sqnums[right]
            if nsum in mp:
                return True
                
    return False
        

print(findPythagoreanTriplets([3, 7, 4, 21, 13, 15, 19, 17, 25, 8]))
# True
