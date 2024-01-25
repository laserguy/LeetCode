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
    unordered_map<int,int> hash;
    int count = 0;
public:
    bool isPalindromePossible(){
        int even_count = 0;
        int odd_count = 0;
        for (auto& pair : hash){
            if (pair.second % 2 == 0) even_count += 1;
            else odd_count += 1;
        }
        
        if (odd_count > 1) return false;
        return true;
    }

    void removeElementFromMap(TreeNode *root){
        if (root != nullptr){
            hash[root->val] -= 1;
            if (hash[root->val] == 0) 
            hash.erase(root->val);
        }
    }

    void traverseAndCount(TreeNode *root){
        if (root == nullptr) return;
        hash[root->val]++;

        if (root->left == nullptr && root->right == nullptr){
            if(isPalindromePossible()) count += 1;
            return;
        }

        traverseAndCount(root->left);
        removeElementFromMap(root->left);
        traverseAndCount(root->right);
        removeElementFromMap(root->right);
    }

    int pseudoPalindromicPaths (TreeNode* root) {
        traverseAndCount(root);
        return count;
    }
};