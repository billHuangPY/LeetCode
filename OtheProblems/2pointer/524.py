class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        member_index = [len(member)-1 for member in dictionary]
        valid_member, valid_length = '', 0

        for c in s[::-1]:
            for member_id in range(len(dictionary)):
                #print(member_id)
                if not member_index[member_id] < 0 and dictionary[member_id][member_index[member_id]] == c:
                    member_index[member_id] -= 1
                    if member_index[member_id] < 0:
                        if len(dictionary[member_id]) > valid_length or (len(dictionary[member_id]) == valid_length and dictionary[member_id] < valid_member):
                            valid_member = dictionary[member_id]
                            valid_length = len(valid_member)
        
        return valid_member
