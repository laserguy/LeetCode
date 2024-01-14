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
    int max_distance = 0;
    int start;
public:
    int traverse(TreeNode *root){
        if (root == nullptr) return 0;

        int depth = 0;
        int ldepth = traverse(root->left);
        int rdepth = traverse(root->right);

        if(root->val == start){
            max_distance = max(ldepth,rdepth);
            depth = -1;
        }
        else if(ldepth >= 0 && rdepth >= 0){
            depth = max(ldepth,rdepth) + 1;
        }
        else{
            int distance = abs(ldepth) + abs(rdepth);
            max_distance = (distance > max_distance) ? distance : max_distance;
            depth = min(ldepth,rdepth) - 1;
        }
        return depth;
    }

    int amountOfTime(TreeNode* root, int start) {
        this->start = start;
        traverse(root);
        return max_distance;
    }
};