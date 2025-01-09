# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"


    def deserialize(self, data: str):
        if not data:
            return None
        q_data = deque(data.split(","))
        return self.deserialize_list(q_data)


    def deserialize_list(self, nums: List[str]):
        val = nums.popleft()
        if not val:
            return None

        root = TreeNode(val)
        root.left = self.deserialize_list(nums)
        root.right = self.deserialize_list(nums)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))