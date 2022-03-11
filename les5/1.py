class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        pre = node
        stack = []
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is pre or not node.right:
                pre = stack.pop()
                res.append(pre.val)
                node = None
            else:
                node = node.right
        return res
