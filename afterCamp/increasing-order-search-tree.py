# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        stack = []

        def makeInorder(root):
            if not root:
                return None
            left = makeInorder(root.left)
            node = TreeNode(root.val)
            if stack:
                stack[-1].right = node
            stack.append(node)
            right = makeInorder(root.right)
        makeInorder(root)

        return stack[0]


