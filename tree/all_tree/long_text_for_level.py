import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result


# 递归法
# Definition for a binary tree node.

class Solution2:
    def __init__(self):
        self.levels = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        self.traverse(root, 0)
        return self.levels

    def traverse(self, node, level):
        if not node:
            return

        if len(self.levels) == level:
            self.levels.append([])

        self.levels[level].append(node.val)
        self.traverse(node.left, level + 1)
        self.traverse(node.right, level + 1)


def create_deep_tree(depth):
    if depth == 0:
        return None

    root = TreeNode(0)
    current_level = [root]

    for i in range(1, depth):
        next_level = []
        for node in current_level:
            node.left = TreeNode(str(i) + '-> ' + 'left')
            node.right = TreeNode(str(i) + '-> ' + 'right')
            next_level.append(node.left)
            next_level.append(node.right)
        current_level = next_level

    return root


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.right = TreeNode(6)
    root = create_deep_tree(4)
    a = Solution().levelOrder(root)
    print(a)
    solution = Solution2()
    result = solution.levelOrder(root)
    print(result)  # 输出应该是 [[1], [2, 3], [4, 5, 6]]
