# Generating all the valid parenthesis: clearly this should be a recursive solution
# TIme complexity for below is O((4^n)/sqrt(n))
# Why: The below approach will create a binary tree with depth 2n, that means 4^n total nodes
# and after pruning we would still be calculating (4^n)/sqrt(n) nodes

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        # s: current parenthesis string 
        # forward: number of forward slashes in the string s
        # backward: number of backward slashes in the string s
        def func(s: str, forward: int, backward: int) -> None:
            nonlocal parenthesis
            # Recursion end consition
            if len(s) == 2*n:
                parenthesis.append(s)
                return
            
            # DOn't add '(' to the string if it exceeds n
            if forward < n:
                func(s+'(', forward+1, backward)
            # Below condition is for the pruning, i.e to add backward slash in case of valid parenthesis
            if backward < forward and backward < n:
                func(s+')', forward,backward+1)

        func("",0,0)
        return parenthesis
