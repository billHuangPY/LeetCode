class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();

        int **dptable;
        dptable = new int *[m+1];
        for (int i=0; i<m+1; i++){
            dptable[i] = new int[n+1];
        }
        
        for (int i=0; i<m+1; i++){
            for (int j=0; j<n+1; j++){
                if (i==0 || j==0){
                    dptable[i][j] = 0;
                    
                }else if(text1[i-1] == text2[j-1]){
                    dptable[i][j] = 1 + dptable[i-1][j-1];
                    //std::cout << text1[i] << " = " << text2[j] << endl; 
                }else{
                    dptable[i][j] = std::max(dptable[i-1][j], dptable[i][j-1]);
                }
                //std::cout << i << " "<< j << " " << dptable[i][j] << endl;
            }
        }
        
        return dptable[m][n];
    }
};