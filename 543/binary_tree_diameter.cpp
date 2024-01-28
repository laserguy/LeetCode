/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int maxD = 0;
public:
    int traverse(TreeNode *root){
        if (root == nullptr) return 0;
        int L = traverse(root->left);
        int R = traverse(root->right);
        if (maxD < (L+R+1))
            maxD = L + R +1;

        return 1 + max(L,R);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        traverse(root);
        return maxD -1;
    }
};