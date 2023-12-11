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
    ListNode* addTwoNumbers(ListNode* first, ListNode* second) {
        int carry = 0;
        ListNode* head = nullptr, *it = nullptr;
        while (first != nullptr || second != nullptr){
            int sum = carry;
            if (first != nullptr){
                sum += first->val;
                first = first->next;
            }
            if (second != nullptr){
                sum += second->val;
                second = second->next;
            }
            carry = int(sum/10);
            sum = sum % 10;
            ListNode* temp = new ListNode(sum);
            if (head == nullptr){
                head = temp;
                it = head;
            }
            else{
                it->next = temp;
                it = it->next;
            }
        }

        if (carry == 1){
            ListNode* temp = new ListNode(carry);
            it->next = temp;
        }

        return head;
    }
};