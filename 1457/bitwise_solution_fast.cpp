class Solution {
    int count = 0;
public:
    void traverseAndCount(TreeNode *root, int path){
        if (root == nullptr) return;
		// Each number represents a bit position, number 7 represents 7th position
		// Instead of storing path in a array/hash(like my solution), we use integer and use bitwise operations to check if the path is a palindrome.
		// If 7 appears in the path then we will set 7th position to 1, if it appears again we will set to zero(Therefore XOR operation), therefore if a bit is odd that means odd number of appearance for 7, if it is even then it means even appearance
        path ^= (1 << root->val);

        if (root->left == nullptr && root->right == nullptr){
			// This checks if path contains atmost 1 bit set to 1
            if((path&(path-1)) == 0) count += 1;
            return;
        }

        traverseAndCount(root->left, path);
        traverseAndCount(root->right, path);
    }

    int pseudoPalindromicPaths (TreeNode* root) {
        traverseAndCount(root,0);
        return count;
    }
};