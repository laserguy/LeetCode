class FoodRatings {
    struct foodNode{
        string food;
        int rating;
        foodNode *next;
        foodNode(string F, int R): food(F), rating(R), next(nullptr){}
    };
    // Map cusine to a linked list of foods in that cusine
    map<string, foodNode *> CusineHash;
    // Using another hash, this would map foodname to the location of its foodNode
    // This makes the function changeRating to operate in O(1)
    map<string, foodNode *> FoodHash;

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i=0; i<foods.size();i++){
            foodNode *node = new foodNode(foods[i], ratings[i]);
            if (CusineHash.find(cuisines[i]) == CusineHash.end()){
                CusineHash[cuisines[i]] = node;
            }
            else{
                foodNode *temp = CusineHash[cuisines[i]];
                node->next = temp;
                CusineHash[cuisines[i]] = node;
            }

            FoodHash[foods[i]] = node;
        }
    }
    
    void changeRating(string food, int newRating) {
        FoodHash[food]->rating = newRating;
    }
    
    string highestRated(string cuisine) {
        foodNode *maxRatedNode = nullptr;
        int maxRating = -1;
        foodNode *node = CusineHash[cuisine];

        while(node != nullptr){
            if (node->rating >= maxRating){
                if (node->rating == maxRating){
                    if (node->food < maxRatedNode->food){
                        maxRatedNode = node;
                    }
                }
                else{
                    maxRating = node->rating;
                    maxRatedNode = node;
                }
            }
            node = node->next;
        }

        return maxRatedNode->food;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */