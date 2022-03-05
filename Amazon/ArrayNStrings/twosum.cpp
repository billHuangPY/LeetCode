#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i ++){
            map[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i ++){
            if (map.find(target - nums[i]) != map.end()) {
                int found = map[target - nums[i]];
                if (found != i)
                    return {(int)i, found};
            }
        }

        return std::vector<int>();
    }

};