'''
This file implements the AVL Tree data structure.
The functions in this file are considerably
harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree():
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that
        all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node == AVLTree.root:
            tree_minimum = BST._find_smallest(node)
            tree_maximum = BST._find_largest(node)
        if node.left:
            if node.value >= tree_minimum:
                tree_maximum = node.left.value
                ret &= AVLTree._is_avl_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= tree_maximum:
                tree_minimum = node.right.value
                ret &= AVLTree._is_avl_satisfied(node.right)
            else:
                ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level
        overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.right is None:
            return node

        root_1 = Node(node.right.value)
        root_1.right = node.right.right
        root_1.left = Node(node.value)
        root_1.left.left = node.left
        root_1.left.right = node.right.left

        return root_1

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level
        overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
         tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.left is None:
            return node

        root_1 = Node(node.left.value)
        root_1.left = node.left.left
        root_1.right = Node(node.value)
        root_1.right.right = node.right
        root_1.right.left = node.left.right

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level
        overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their
        AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions
        for this code.
        The code should look very similar to the
        code for your insert function for the BST,
        but it will also call the left and right
        rebalancing functions.
        '''
        if self.root:
            return AVLTree._insert(self.root, value)
        return True

    @staticmethod
    def _insert(root, value):
        if not root:
            return Node(value)
        else:
            if root.value == value:
                return root
            elif root.value < value:
                root.right = AVLTree._insert(root.right, value)
            else:
                root.left = AVLTree._insert(root.left, value)
        return root

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)
