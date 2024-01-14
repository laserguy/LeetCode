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
    unordered_map<int, vector<int>> graph;
public:
    void convert(TreeNode *root, int parent){
        if(root == nullptr) return;

        vector<int> t;
        if(parent != 0) t.push_back(parent);
        if(root->left) t.push_back(root->left->val);
        if(root->right) t.push_back(root->right->val);

        this->graph[root->val] = t;
        convert(root->left,root->val);
        convert(root->right,root->val);
    }
    
    void printGraph(){
        for (const auto &key: graph){
            cout << key.first << ":";
            for(const auto &e : key.second)
                cout << e << " ";
            cout << endl;
        }
    }

    int amountOfTime(TreeNode* root, int start) {
        convert(root,0);
        //printGraph();

        unordered_map<int,bool> visited;
        queue<int> q;
        q.push(start);
        visited[start] = true;
        int minute = 0;

        while(!q.empty()){
            int size = q.size();
            while(size--){
                int x = q.front();
                q.pop();

                for (const auto &num : graph[x]){
                    if(visited.find(num) == visited.end()){
                        visited[num] = true;
                        q.push(num);
                    }
                }
            }
            minute += 1;
        }
        return minute-1;
    }
};