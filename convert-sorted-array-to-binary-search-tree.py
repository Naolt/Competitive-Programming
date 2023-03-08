# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = None
        return self.constructTree(nums,root)

    def insertNode(self,root,val):
        if not root:
            node = TreeNode(val,None,None)
            return node
        if val > root.val:
            root.right = self.insertNode(root.right,val)
        else:
            root.left = self.insertNode(root.left,val) 
        return root
    def constructTree(self,nums,root):
        if not nums:
            return root
        if len(nums) == 1:
            return self.insertNode(root,nums[0])

        mid = len(nums)//2
        print(nums,mid)
        node = self.insertNode(root,nums[mid])
        self.constructTree(nums[0:mid],node)
        self.constructTree(nums[mid+1:len(nums)],node)
        
        return node