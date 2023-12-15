#include<map>

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node *out = NULL;
        map<Node *, Node *> hashmap;

        while(head != NULL){
            Node *temp = new Node(head->val);
            hashmap[head] = temp;
            if (out == NULL) out = temp;

            head = head->next;
        }

        map<Node *, Node *>::iterator it;
        for (it = hashmap.begin(); it!= hashmap.end(); it++){
            it->second->next = hashmap[it->first->next];
            it->second->random = hashmap[it->first->random];
        }

        return out;
    }
};