/*
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
*/

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> newVec;
        if(matrix.size() == 0){
            return newVec;
        }

        int M = matrix.size()-1, N = matrix[0].size()-1;
        //int xmax, ymax, xmin, ymin;
        for (int MNsum = 0; MNsum <= M+N; MNsum ++){
            if(MNsum % 2 == 0){
                for(int i = 0; i <= MNsum; i ++){
                    if(MNsum-i < 0 || MNsum-i > M){
                        continue;
                    }
                    if(i > N){
                        continue;
                    }

                    cout << MNsum-i << " " << i << endl;
                    newVec.push_back(matrix[MNsum-i][i]);
                }
            }else{
                for(int i = 0; i <= MNsum; i++){
                    if(MNsum-i < 0 || MNsum-i > N){
                        continue;
                    }
                    if(i > M){
                        continue;
                    }
                    cout << i << " " << MNsum-i << endl;
                    newVec.push_back(matrix[i][MNsum-i]);
                }
            }
        }
        
        return newVec;
    }
};