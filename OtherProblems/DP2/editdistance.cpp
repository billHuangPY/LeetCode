class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.length();
        int m = word2.length();
        
        int **dptable;
        dptable = new int *[n+1];
        for (int i = 0; i < n+1; i++){
            dptable[i] = new int[m+1];
        }
        for (int i = 0; i < n+1; i++){
            dptable[i][0] = i;
        }
        for (int i = 0; i < m+1; i++){
            dptable[0][i] = i;
        }

        for (int i = 1; i < n+1; i++){
            for (int j = 1; j < m+1; j++){
                if (word1[i-1] == word2[j-1]){
                    dptable[i][j] = 1 + std::min(std::min(dptable[i-1][j-1]-1, dptable[i][j-1]), dptable[i-1][j]);
                } else {
                    dptable[i][j] = 1 + std::min(std::min(dptable[i-1][j-1], dptable[i][j-1]), dptable[i-1][j]);
                }
            }
        }

        return dptable[n][m];

    }
};