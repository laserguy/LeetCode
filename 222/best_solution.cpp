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
    int depth;
    bool leafBeforeDepth = false;
public:
    int leftDepth(TreeNode *root){
        if (root == nullptr) return 0;
        return 1 + leftDepth(root->left);
    }

    int rightDepth(TreeNode *root){
        if (root == nullptr) return 0;
        return 1 + rightDepth(root->right);
    }

    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        int ldepth = leftDepth(root);
        int rdepth = rightDepth(root);

        if (ldepth == rdepth) return pow(2,ldepth) - 1;
        
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};