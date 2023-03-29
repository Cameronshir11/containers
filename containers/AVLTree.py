'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the
functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
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
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function. - invariant
        Use balance_factor(node) this uses the height.
        '''
        if node is None:
            return True
        # Check if balance factor is outside of [-1, 0, 1]
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
         # Recursively check left and right subtrees
        left_subtree_satisfied = AVLTree._is_avl_satisfied(node.left)
        right_subtree_satisfied = AVLTree._is_avl_satisfied(node.right)
        return left_subtree_satisfied and right_subtree_satisfied

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        Modify Code will need to store node so the nodes do not have any explicit links to their parents
        so instead of modifying the original tree. Fix our code so it prints a new tree
        '''
        origRoot = node
        if origRoot.right:
            newRoot = Node(origRoot.right.value)
            newRoot.left = Node(origRoot.value)
            newRoot.right = origRoot.right.right
            newRoot.left.left = origRoot.left
            newRoot.left.right = origRoot.right.left
            return newRoot
        else:
            return origRoot

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        origRoot = node
        if origRoot.left:
            newRoot = Node(origRoot.left.value)
            newRoot.right = Node(origRoot.value)
            newRoot.left = origRoot.left.left
            newRoot.right.right = origRoot.right
            newRoot.right.left = origRoot.left.right
            return newRoot
        else:
            return origRoot

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        '''
        if node is None:
            return Node(value)
        if node.value == value:
            return
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        node.height = 1 + max(AVLTree._height(node.left), AVLTree._height(node.right))
        node = AVLTree._rebalance(node)

        return node
        '''
        '''
        if node.value == value:
            return
        if value < node .value:
            if node.left is None:
                node.left = Node(value)
            else:
                return AVLTree._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                return AVLTree._insert(value, node.right)
        else:
            print('Cannot insert')
        if AVLTree._is_avl_satisfied(node) == False:
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            return AVLTree._rebalance(node)
        '''
        if not node:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node:
            balance_factor = AVLTree._balance_factor(node)
        if balance_factor > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._right_rotate(node.right)
            node = AVLTree._left_rotate(node)
        elif balance_factor < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            node = AVLTree._balance_factor(node)
        return node

        '''
        if node._balance_factor < -1:
            if node.right._balance_factor > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            else:
                AVLTree._left_rotate(node)
        elif node._balance_factor > 1:
            if node.left._balance_factor < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            else:
                AVLTree._right_rotate(node)
        '''
