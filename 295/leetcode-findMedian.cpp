#include <iostream>
using namespace std;

class MedianFinder {
    struct node {
        int val;
        node *next;
        node() : val(0), next(nullptr) {}
        node(int x) : val(x), next(nullptr) {}
        node(int x, node *next) : val(x), next(next) {}
    };
    node *head;
    int size;
public:
    MedianFinder() {
        head = NULL;
        size = 0;
    }

    void insert_into_linked_list(int num){
        if(head == NULL){
            head = new node(num);
            return;
        }

        node *prev = NULL;
        node *fast = head;
        while(fast != NULL){
            if(fast->val < num){
                prev = fast;
                fast = fast->next;
            }
            else{
                break;
            }
        }

        node *temp = new node(num);
        if(prev == NULL){
            temp->next = head;
            head = temp;
        }
        else{
            prev->next = temp;
            temp->next = fast;
        }
    }

    void addNum(int num) {
        insert_into_linked_list(num);
        size +=1;
    }
    
    double findMedian() {
        node *start = head;
        if(size%2 != 0){
            int count = size/2 + 1;
            while(count--){
                start = start->next;
            }
            return float(start->val);
        }
        else{
            int count = size/2;
            while(count--){
                start = start->next;
            }

            double output = start->val + start->next->val;
            return (output)/2;
        }
    }
};

int main() {
	MedianFinder* obj = new MedianFinder();
	obj->addNum(2);
	double param_2 = obj->findMedian();
	return 0;
}