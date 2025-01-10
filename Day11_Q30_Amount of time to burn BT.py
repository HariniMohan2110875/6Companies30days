
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {root.val: None}
        depth = defaultdict(int) 
        p = None

   
        def dfs(node):
            nonlocal p
            if not node:
                return
            if node.val == start:
                p = node
            depth[node.val] = 0
            if node.left:
                parents[node.left.val] = node
                dfs(node.left)
                depth[node.val] = depth[node.left.val] + 1
            if node.right:
                parents[node.right.val] = node
                dfs(node.right)
                depth[node.val] = max(depth[node.right.val] + 1, depth[node.val])

        dfs(root)
        ans, i = depth[start], 1
        while p and parents[p.val]:
            parent = parents[p.val]
            sibling = parent.left if p == parent.right else parent.right
            if sibling:
 
                ans = max(ans, depth[sibling.val] + i + 1)
            else:  
                ans = max(ans, i)
            i += 1
            p = parent
        return ans
