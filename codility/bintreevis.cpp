// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(tree * T) {
    // write your code in C++14 (g++ 6.2.0)
    if (!T) return 0;
    return findvisible(T, -10^6);
}

int findvisible(tree * T, int maxroot){
    int visnum = 0;
    int top = maxroot;

    if (T -> x > top){
        top = T -> x;
        visnum += 1;
    }

    if (T -> l){
        visnum += findvisible(T -> l, top);
    }
    if (T -> r){
        visnum += findvisible(T -> r, top);
    }
    return visnum;
}
