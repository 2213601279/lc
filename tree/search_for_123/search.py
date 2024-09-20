from typing import List

from caculate.tree.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if node is None:
                return
            # 修改这里就行
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res