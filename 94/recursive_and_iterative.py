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
#include <stack>

class Solution {
    vector<int> inorderTree;
    void traverseInorder(TreeNode *root){
        if(root == nullptr) return;

        traverseInorder(root->left);
        inorderTree.push_back(root->val);
        traverseInorder(root->right);
    }
public:
    // vector<int> inorderTraversal(TreeNode* root) {
    //     traverseInorder(root);
    //     return inorderTree;
    // }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> inorderTree;
        stack<TreeNode*> stack;

        while(root != nullptr){
            while(root != nullptr){
                stack.push(root);
                root = root->left;
            }
            while(root == nullptr && !stack.empty()){
                TreeNode* e = stack.top();
                stack.pop();
                inorderTree.push_back(e->val);
                root = e->right;
            }
        }

        return inorderTree;
    }
};