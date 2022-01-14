class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_num = 1
        curr_left, curr_right = 0, 0
        curr_fruit = {fruits[0]:1}
        
        while curr_right <= len(fruits):
            if len(curr_fruit) <= 2:
                max_num = max(max_num, curr_right - curr_left + 1)
                    
                curr_right += 1
                if curr_right == len(fruits):
                    break
                    
                if fruits[curr_right] in curr_fruit:
                    curr_fruit[fruits[curr_right]] += 1
                else:
                    curr_fruit[fruits[curr_right]] = 1
            
            else:
                if curr_fruit[fruits[curr_left]] == 1:
                    del curr_fruit[fruits[curr_left]]
                else:
                    curr_fruit[fruits[curr_left]] -= 1
                    
                curr_left += 1
        
        return max_num
                
                
            
        
        
        