"""
Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise,
the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

"""


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_child(self, val):
        if val == self.val:
            return

        if val < self.val:
            if self.left:
                self.left.add_child(val=val)
            else:
                self.left = TreeNode(val=val)
        else:
            if self.right:
                self.right.add_child(val=val)
            else:
                self.right = TreeNode(val=val)


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = TreeNode()
        if not t1:
            return t2
        if not t2:
            return t1

        t3.val = t1.val + t2.val

        t3.left = self.mergeTrees(t1.left, t2.left)
        t3.right = self.mergeTrees(t1.right, t2.right)
        return t3


def construct_bst(elements):
    tree = TreeNode(elements[0])
    for e in elements:
        tree.add_child(e)

    return tree


if __name__ == "__main__":
    n1 = [3, 5, 7]
    n2 = [2, 1, 3]
    tree1 = construct_bst(elements=n1)
    tree2 = construct_bst(elements=n2)
    solution = Solution()
    tree3 = solution.mergeTrees(t1=tree1, t2=tree2)
