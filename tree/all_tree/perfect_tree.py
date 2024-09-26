"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


def create_deep_tree(depth):
    """
    创建二叉树
    :param depth:
    :return:
    """
    if depth == 0:
        return None

    root = Node(0)
    current_level = [root]
    count = 0
    for i in range(1, depth):
        next_level = []
        for node in current_level:
            count += 1
            node.left = Node(str(count) + '-> ' + 'left')
            count += 1
            node.right = Node(str(count) + '-> ' + 'right')
            node.next = Node(str(count) + '-> ' + 'next')
            next_level.append(node.left)
            next_level.append(node.right)
        current_level = next_level

    return root


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for i in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root

    def connect_II(self, root: Node) -> Node:
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for i in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


if __name__ == '__main__':
    root = create_deep_tree(5)
    print(Solution().connect_II(root))
