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
    int getDepth(TreeNode *root){
        if (root == nullptr) return 0;
        return 1 + getDepth(root->left);
    }

    int countLeavesAtDepth(TreeNode *root, int level){
        if (root == nullptr) return 0;
        if (root->left == nullptr && root->right == nullptr){
            if (level == depth) return 1;
            else {
                leafBeforeDepth = true;
                return 0;
            }
        }
        else if (root->left != nullptr && root->right == nullptr){
            leafBeforeDepth = true;
            return 1;
        }

        int count = 0;
        if (leafBeforeDepth == false) count += countLeavesAtDepth(root->left, level + 1);
        if (leafBeforeDepth == false) count += countLeavesAtDepth(root->right, level + 1);

        return count;
    }

    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;

        depth = getDepth(root);
        cout << depth;
        int leaves = countLeavesAtDepth(root, 1);

        return pow(2,depth-1) + leaves - 1;
    }
};