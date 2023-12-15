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
        if (head == NULL) return NULL;
        if (head->next == NULL){
            Node *temp = new Node(head->val);
            if (head->random != NULL) temp->random = temp;
            return temp;
        }
        Node *node = head, *next_ = NULL;

        while(node != NULL){
            Node *temp = new Node(node->val);
            next_ = node->next;
            node->next = temp;
            temp->next = next_;
            node = next_;
        }
        
        Node *first = head, *second = head->next;

        while(first != NULL && first->next != NULL){
            if (first->random != nullptr){
                second->random = first->random->next;
            }
            first = first->next->next;
            if (first != NULL) second = first->next;
        }

        first = head;
        second = head->next;
        Node *newH = second;

        while(second != NULL && second->next != NULL){
            first->next = first->next->next;
            second->next = second->next->next;
            first = first->next;
            second = first->next;
            if (second->next == NULL) first->next = NULL;
        }

        return newH;
    }
};