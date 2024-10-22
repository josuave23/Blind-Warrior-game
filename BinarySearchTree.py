from BinaryTree import BinaryTree
from Interfaces import Set

class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        """
        BinarySearchTree constructor; initializes an empty binary search tree
        """
        super().__init__()
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        Adds a new node with the given key and value to the tree if the key doesn't already exist.
        :param key: object type; the key of the new node
        :param value: object type; the value associated with the key (optional)
        :return: bool type; True if the key-value pair was added to the tree, False otherwise.
        """
        if self._add_child(self._find_last(key), self.Node(key, value)):
            self.n += 1
            return True
        return False

    def find(self, key: object) -> object:
        """
        Finds and returns the value corresponding to the given key if it exists in the BinarySearchTree.
        :param key: object type; the key to search for
        :return: object type or None; the value corresponding to the given key if it exists, None otherwise.
        """
        node = self._find_eq(key)
        return node.v if node else None

    def remove(self, key: object):
        """
        Removes the node with the given key if it exists in this BinarySearchTree.
        :param key: object type; the key to remove
        :return: object type; the value corresponding to the removed key, if the key was in the tree.
        :raises: ValueError if the given key does not exist in the tree
        """
        node = self._find_eq(key)
        if node is None:
            raise ValueError(f"Key {key} not found")
        removed_value = self._remove_node(node)
        self.n -= 1
        return removed_value

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        Helper method to find(key); returns the node in this tree that contains the given key, or None otherwise.
        """
        u = self.r
        while u is not None:
            cmp = (key > u.k) - (key < u.k)
            if cmp == 0:
                return u
            u = u.right if cmp > 0 else u.left
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        Helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node with the given key, if it existed
        """
        w = self.r
        prev = None
        while w is not None:
            prev = w
            cmp = (key > w.k) - (key < w.k)
            if cmp == 0:
                return w
            w = w.right if cmp > 0 else w.left
        return prev

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        Helper method to add(key, val); adds node u as the child of node p,
        assuming node p has at most 1 child, and the invariant will not be violated
        """
        if p is None:
            self.r = u
        else:
            cmp = (u.k > p.k) - (u.k < p.k)
            if cmp == 0:
                return False
            if cmp > 0:
                p.right = u
            else:
                p.left = u
            u.parent = p
        return True

    def _splice(self, u: BinaryTree.Node):
        """
        Helper method to remove(key); links the parent of given node u to the child
        of node u, assuming u only has one child
        """
        parent = u.parent
        child = u.left if u.left is not None else u.right
        if parent is None:
            self.r = child
        elif parent.left == u:
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

    def _remove_node(self, u: BinaryTree.Node):
        removed_value = u.v  
        if u.left is None or u.right is None:
            self._splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.k, w.k = w.k, u.k
            u.v, w.v = w.v, u.v
            self._splice(w)
        return removed_value  


    def clear(self):
        """
        Empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    def bookstore_helper(self, prefix: str):
        u = self.r
        while u is not None:
            if u.k.startswith(prefix):
                return u
            elif prefix < u.k:
                u = u.left
            else:
                u = u.right
        return None
