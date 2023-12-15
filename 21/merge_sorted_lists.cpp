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
    ListNode* mergeTwoLists(ListNode* first, ListNode* second) {
        if (first == nullptr) return second;
        if (second == nullptr) return first;

        ListNode *head= nullptr, *it = nullptr;

        while (first != nullptr and second != nullptr){
            ListNode *temp = nullptr;
            if (first->val <= second->val){
                temp = first;
                first = first->next;
            }
            else{
                temp = second;
                second = second->next;
            }

            if (head == nullptr){
                head = temp;
                it = head;
            }
            else{
                it->next = temp;
                it = it->next;
            }
        }

        if(first != nullptr) it->next = first;
        else if (second != nullptr) it->next = second;

        return head;
    }
};