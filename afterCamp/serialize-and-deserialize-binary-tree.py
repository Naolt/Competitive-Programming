# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            serial.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(list(map(str,serial)))


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serial = data.split(',')
        serial = list(map(lambda x: None if x == "None" else TreeNode(int(x)),serial))
        
        nulls = 0
        for i in range(len(serial)):
            left = ((i+1)*2 - 1) - nulls
            right = ((i+1)*2) - nulls
            if not serial[i]:
                nulls += 2
                continue
            if left < len(serial):
                serial[i].left = serial[left]
            if right < len(serial):
                serial[i].right = serial[right]


        return serial[0]

        

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))