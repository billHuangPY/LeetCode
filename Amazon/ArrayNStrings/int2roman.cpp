#include <vector>
#include <string>
#include <math.h>

class Solution {
public:
    std::string intToRoman(int num) {
        const std::string dict[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        const int value[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        std::string ans;
        int m, q = num;

        for (int i = 0; i < 13 && q > 0; i ++) {
            m = q / value[i];
            for (int j = 0; j < m; j ++) 
                ans += dict[i];
            q = q % value[i];
        }

        return ans;
        
        
    }
};