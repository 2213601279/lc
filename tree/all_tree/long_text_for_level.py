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
    """
    创建二叉树
    :param depth:
    :return:
    """
    if depth == 0:
        return None

    root = TreeNode(0)
    current_level = [root]
    count = 0
    for i in range(1, depth):
        next_level = []
        for node in current_level:
            count += 1
            node.left = TreeNode(str(count) + '-> ' + 'left')
            count += 1
            node.right = TreeNode(str(count) + '-> ' + 'right')
            next_level.append(node.left)
            next_level.append(node.right)
        current_level = next_level

    return root


class Solution_bottom_to_top:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return result[::-1]


class Solution_rightSideView:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        right_view = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    right_view.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view


class SolutionaverageOfLevels:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        queue = collections.deque([root])
        averages = []

        while queue:
            size = len(queue)
            level_sum = 0

            for i in range(size):
                node = queue.popleft()
                if type(node.val) != int:
                    node.val = int(node.val.split('-> ')[0])
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / size)

        return averages


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

    print(result[::-1])  # 输出应该是 [[1], [2, 3], [4, 5, 6]]

    ax = Solution_bottom_to_top().levelOrderBottom(root)
    print(ax)
    print()
    print(Solution_rightSideView().rightSideView(root))
    print(SolutionaverageOfLevels().averageOfLevels(root))
