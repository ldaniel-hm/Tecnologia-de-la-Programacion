from typing import Optional

def tree(funcion):
    def g(*args, **kawargs):
        funcion(*args, **kwargs)
    return g

class NodeBinaryTree:
    def __init__(self, value: Optional[float]=None, left:Optional['NodeBinaryTree'] = None, right:Optional['NodeBinaryTree'] = None):
        self._value = value
        self._left = left
        self._right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self) -> 'NodeBinaryTree':
        return self._left

    @left.setter
    def left(self, left:Optional['NodeBinaryTree']):
        self._left = left

    @property
    def right(self) -> 'NodeBinaryTree':
        return self._right

    @right.setter
    def right(self, right:Optional['NodeBinaryTree']):
        self._right = right

    def __str__(self):
        string = str(self._value)
        if self.left:
            string = string + "->" + str(self.left)
        if self.right:
            string = string + "  <-" + str(self.right)
        return string

class SearchTree:
    def __init__(self):
        self._root: Optional[NodeBinaryTree] = None

    def is_empty(self) -> bool:
        return self._root

    def add(self, value: float):
        if self._root:
            self._root.add(value)
        else:
            self._root = NodeBinaryTree(value)


    def append(self, value: float):
        self._root = self._append(self._root, value)

    def _append(self, root: NodeBinaryTree, value: float):
        if root is None:
            return NodeBinaryTree(value)

        if value < root.value:
            root.left = self._append(root.left, value)
        elif value > root.value:
            root.right = self._append(root.right, value)
        else:
            return root

    def search(self, value: float):
        return self._search(self._root, value)

    def _search(self, root, value) -> bool:
        if root is None:
            return False

        if root.value == value:
            return True

        if value < root.value:
            return self._search(root.left, value)

        return self._search(root.right, value)



    def remove(self, value: float):
       self._root = self._remove(self._root, value)

    def _remove(self, root: NodeBinaryTree, value: float):
        if root is None:
            return None

        if value < root.value:
            root.left = self._remove(root.left, value)
        elif value > root.value:
            root.right = self._remove(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            root.value = self._find_min_value(root.right)
            root.right = self._remove(root.right, root.value)
        return root

    def _find_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value


    def __str__(self):
        return str(self._root)


tree = SearchTree()
l = [8, 3, 10, 1, 6, 4, 7, 14, 12, 13, 9]
for x in l:
    tree.add(x)

tree.remove(12)
print(tree)

