class Solution:
    ## not optimal
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        
        s_list = []
        for i in range(len(s)-word_size+1):
            if s[i:i+word_size] in words:
                s_list.append([i, i+word_size, s[i:i+word_size]])
        word_list = {}
        for word in words:
            if word in word_list:
                word_list[word] += 1
            else:
                word_list[word] = 1
        
        ## print(s_list)
                
        ans_list = []
        for index in range(len(s_list)-len(words)+1):
            word_list_tmp, length = {}, 1
            word_list_tmp = word_list.copy()
            word_list_tmp[s_list[index][2]] -= 1
            
            ## print(word_list_tmp)
            
            curr = index
            for j in range(index+1, len(s_list)):
                if s_list[j][0] > s_list[curr][1]:
                    break
                if s_list[j][0] < s_list[curr][1]:
                    continue
                if word_list_tmp[s_list[j][2]] > 0:
                    word_list_tmp[s_list[j][2]] -= 1
                    length += 1
                    curr = j
                
            if length == len(words):
                ans_list.append(s_list[index][0])
                
        return ans_list
        