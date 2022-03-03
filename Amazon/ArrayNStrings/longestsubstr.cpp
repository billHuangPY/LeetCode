#include <algorithm>
#include <unordered_map>
#include <string>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int left = 0, right = 0;
        std::unordered_map<char, int> map;

        int ans = 0;
        while (right < s.length()) {
            char r = s[right];
            if (map.count(r) > 0)
                map[r] ++;
            else
                map[r] = 1;
            
            while (map[r] > 1) {
                char l = s[left];
                map[l] --;
                left ++;
            }

            ans = std::max(ans, right - left + 1);
            right ++;
        }

        return ans;
    }
};