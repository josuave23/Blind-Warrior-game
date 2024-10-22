import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"

    def __init__(self):
        """
        BinaryTree constructor; initializes an empty binary tree
        """
        self.r = None

    def depth(self, u: Node) -> int:
        """
        returns the path length between the root and the given node.
        :param u: Node type; the node of interest
        :return: int type; the depth of the given node
        """
        depth_count = 0
        while u != self.r:
            u = u.parent
            depth_count += 1
        return depth_count

    def height(self) -> int:
        """
        returns the height of this binary tree, i.e. the length of the
        longest path that exists from the root to a leaf node.
        :return: int type;
        """
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        """
        helper method; returns the height of the subtree rooted at the given node.
        :param u: Node type; the node of interest
        :return: int type;
        """
        if u is None:
            return -1
        left_height = self._height(u.left)
        right_height = self._height(u.right)
        return max(left_height, right_height) + 1

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        """
        helper method for size(); returns the size of the subtree
        rooted at the given node.
        :param u: Node type; the root of the subtree
        """
        if u is None:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def bf_order(self):
        """
        returns a list of nodes as they are traversed in breadth-first order
        :return: list type; a list of Node objects
        """
        result = []
        if self.r is None:
            return result

        q = SLLQueue.SLLQueue()
        q.add(self.r)

        while q.size() > 0:
            node = q.remove()
            result.append(node)
            if node.left:
                q.add(node.left)
            if node.right:
                q.add(node.right)

        return result

    def in_order(self) -> list:
        """
        returns a list of all nodes in the tree as they are
        traversed using in-order traversal
        :return: list type; a list of Node objects
        """
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        """
        helper method for in_order(); returns the list nodes
        in the subtree rooted at the given node, as they are traversed
        using in-order traversal
        :param u: Node type; the root of the subtree
        """
        if u is None:
            return []
        return self._in_order(u.left) + [u] + self._in_order(u.right)

    def post_order(self) -> list:
        """
        returns a list of all nodes in the tree as they are
        traversed using post-order traversal
        :return: list type; a list of Node objects
        """
        return self._post_order(self.r)

    def _post_order(self, u: Node) -> list:
        """
        helper method for post_order(); returns the list nodes
        in the subtree rooted at the given node, as they are traversed
        using post-order traversal
        :param u: Node type; the root of the subtree
        """
        if u is None:
            return []
        return self._post_order(u.left) + self._post_order(u.right) + [u]

    def pre_order(self) -> list:
        """
        returns a list of all nodes in the tree as they are
        traversed using pre-order traversal
        :return: list type; a list of Node objects
        """
        return self._pre_order(self.r)

    def _pre_order(self, u: Node) -> list:
        """
        helper method for pre_order(); returns the list nodes
        in the subtree rooted at the given node, as they are traversed
        using pre-order traversal
        :param u: Node type; the root of the subtree
        """
        if u is None:
            return []
        return [u] + self._pre_order(u.left) + self._pre_order(u.right)

    def __str__(self):
        """
        returns a string of the nodes as they are traversed using BF order
        :return: str type;
        """
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)
