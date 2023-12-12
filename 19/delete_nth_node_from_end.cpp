/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *first = head, *second = head;
        while(second != nullptr && n > 0){
            second = second->next;
            n -= 1;
        }
        // If n == length of LinkedList
        if(second == nullptr){
            head = head->next;
            delete(first);
            return head;
        }

        while(second->next != nullptr){
            first = first->next;
            second = second->next;
        }

        ListNode *temp = first->next;
        first->next = temp->next;
        delete(temp);
        return head;
    }
};