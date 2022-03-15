class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        dat_root = [root]
        while dat_root:
            for i in range(1, len(dat_root)):
                dat_root[i-1].next = dat_root[i]
            dat_root = [kid for node in dat_root for kid in (node.left, node.right) if kid]
            
        return root
