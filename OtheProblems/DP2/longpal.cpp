class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        bool **dptable;
        dptable = new bool *[n];
        for (int i = 0; i < n; i++){
            dptable[i] = new bool[n];
        }
        
        for (int i = 0; i < n; i++){
            //std::cout << i << " " << i << " true" << endl;
            dptable[i][i] = true;
        }

        int lenmax = 1;
        int maxi = 0;
        for (int i = 1; i < n; i++){
            for (int j = 0; j < n-i; j++){
                if (s[j] == s[j+i]){
                    if (i==1){
                        dptable[j][j+i] = true;
                        //std::cout << j << " " << j+i << " true" << endl;
                    } else {
                        dptable[j][j+i] = dptable[j+1][j+i-1];
                        /*
                        if (dptable[j][j+i]){
                            std::cout << j << " " << j+i << " true" << endl;
                        }*/
                    }
                    if (dptable[j][j+i]){
                        if (i+1 > lenmax){
                            lenmax = i+1;
                            maxi = j;
                        }
                    }
                } else{
                    //std::cout << j << " " << j+i << " false" << endl;
                    dptable[j][j+i] = false;
                }
            }
        }

        return s.substr(maxi, lenmax);
    }
    
};