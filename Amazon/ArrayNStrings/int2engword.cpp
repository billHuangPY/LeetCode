#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>

std::unordered_map<int, std::string> mapless1000;
        
class Solution {
public:
    std::string numberToWords(int num) {
        std::string larger1000[3] = {" Thousand", " Million", " Billion"};

        buildmap();
        if (num == 0)
            return "Zero";
        
        int tmp = num, level = 0;
        
        std::string result = "";
        while (tmp >= 1000) {
            int mod = tmp % 1000;
            result = lessthanthousandsn2w(mod) + result;
            tmp = tmp / 1000;
            if (tmp > 0 && tmp % 1000 > 0) {
                result = larger1000[level] + result;
            }
            level ++;
        }
        if (tmp > 0) 
            result = lessthanthousandsn2w(tmp) + result;

        return result.substr(1,result.length()-1);
    }

    std::string lessthanthousandsn2w(int num) {
        //std::cout << num << std::endl;
        std::string result = "";
        int tmp = num;
        if (tmp >= 100) {
            result = result + mapless1000[tmp/100] + " Hundred";
            tmp = tmp % 100;
        }
        if (tmp > 20) {
            result = result + mapless1000[(tmp/10)*10];
            tmp = tmp % 10;
        }
        if (tmp > 0) {
            result = result + mapless1000[tmp];
        }
        //std::cout << result << std::endl;
        return result;
    }

    void buildmap() {
        mapless1000[90] = " Ninety";
        mapless1000[80] = " Eighty";
        mapless1000[70] = " Seventy";
        mapless1000[60] = " Sixty";
        mapless1000[50] = " Fifty";
        mapless1000[40] = " Forty";
        mapless1000[30] = " Thirty";
        mapless1000[20] = " Twenty";
        mapless1000[19] = " Nineteen";
        mapless1000[18] = " Eighteen";
        mapless1000[17] = " Seventeen";
        mapless1000[16] = " Sixteen";
        mapless1000[15] = " Fifteen";
        mapless1000[14] = " Fourteen";
        mapless1000[13] = " Thirteen";
        mapless1000[12] = " Twelve";
        mapless1000[11] = " Eleven";
        mapless1000[10] = " Ten";
        mapless1000[9] = " Nine";
        mapless1000[8] = " Eight";
        mapless1000[7] = " Seven";
        mapless1000[6] = " Six";
        mapless1000[5] = " Five";
        mapless1000[4] = " Four";
        mapless1000[3] = " Three";
        mapless1000[2] = " Two";
        mapless1000[1] = " One";
    }
};