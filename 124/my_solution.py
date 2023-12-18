# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_overall = -10**10
        def maxPath(root) -> list:
            nonlocal max_overall
            if root == None: return [0,0,0]
            if root.left == None and root.right == None:
                if root.val > max_overall: max_overall = root.val
                return [root.val,root.val,root.val]

            L = maxPath(root.left)
            R = maxPath(root.right)
            X = max(L[1],L[2]) if max(L[1],L[2]) > 0 else 0
            Y = max(R[1],R[2]) if max(R[1],R[2]) > 0 else 0
            A = root.val + X + Y
            B = root.val + X
            C = root.val + Y
            
            max_now = max([root.val,A,B,C])

            if max_now > max_overall:
                max_overall = max_now
            
            return [A,B,C]

        maxPath(root)
        return max_overall