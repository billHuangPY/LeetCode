// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    int ans = 10^7;
    for (int i = 1; i > -1; i --){
        int num = 0;
        if (A.size() % 2 == 0){
            A.push_back(1001);
        }
        for (int j = 1; j < A.size(); j += 2){
            if (A[j] >= A[j-1] || A[j] >= A[j+1]){
                num ++;
            }
        }
        if (num < ans) ans = num;
        if (A.back() == 1001) A.pop_back();
        A.push_front(1001);
    }
    return ans;
}
