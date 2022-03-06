#include <cstddef>
#include <iostream>

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validBSTwithRange(root, LONG_MIN, LONG_MAX);
    }

    bool validBSTwithRange(TreeNode* root, long low, long high) {
        if (!root)
            return true;

        long val = root -> val;
        
        if ((val <= low) or 
            (val >= high))
            return false;

        return (validBSTwithRange(root -> left, low, val)) 
            && (validBSTwithRange(root -> right, val, high));
    }
};