#include <cstddef>
#include <vector>

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
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> ans;
        std::vector<TreeNode*> stk;

        if (!root) return ans;

        stk.push_back(root);
        while (stk.size() > 0) {
            std::vector<int> list;
            std::vector<TreeNode*> sub_stk;
            
            for (int i = stk.size() - 1; i >= 0; i --) {
                list.push_back(stk[i] -> val);
                if (stk[i] -> left) sub_stk.push_back(stk[i] -> left);
                if (stk[i] -> right) sub_stk.push_back(stk[i] -> right);
                stk.pop_back();
            }

            ans.push_back(list);
            std::reverse(sub_stk.begin(), sub_stk.end());
            stk = sub_stk;
        }

        return ans;
    }
};