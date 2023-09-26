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
        
        encodedString = []
        def encodeNodes(node):
            if not node:
                encodedString.append("N")
                return
            encodedString.append(str(node.val))
            encodeNodes(node.left)
            encodeNodes(node.right)
        
        encodeNodes(root)
        return ",".join(encodedString)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        decodedString = data.split(",")
        self.i = 0
        
        def buildTree():
            if decodedString[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(decodedString[self.i]))
            self.i += 1
            node.left = buildTree()
            node.right = buildTree()
            return node
        
        return buildTree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))