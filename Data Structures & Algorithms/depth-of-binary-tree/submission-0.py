# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if not root:
            return 0
        stack.append((root.left,2))
        stack.append((root.right,2))
        maxDepth = 1
        while stack:
            curr, currDepth = stack.pop()
            if not curr:
                continue
            if maxDepth < currDepth:
                maxDepth = currDepth
            stack.append((curr.left,currDepth+1))
            stack.append((curr.right,currDepth+1))
            #print(curr.val, currDepth)

        return maxDepth