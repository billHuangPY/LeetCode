#include <string>
#include <limits.h>
#include <math.h>

class Solution {
public:
    int myAtoi(std::string s) {
        long ans = 0;
        int index = 0, sign = 1;

        while (index < s.size() && s[index] == ' ')
            index ++;
        
        if (index < s.size() && s[index] == '+' || s[index] == '-'){
            if (s[index] == '-')
                sign = -1;
            index ++;
        }
        for (;index < s.size() && s[index] - '0' < 10 && s[index] - '0' >= 0 ; index ++){
            ans = ans * 10 + (s[index] - '0');
            if (sign > 0 && ans > INT_MAX) return INT_MAX;
            if (sign < 0 && -ans < INT_MIN) return INT_MIN;
        }

        return ans*sign;
    }
};