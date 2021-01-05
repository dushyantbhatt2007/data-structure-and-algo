"""
Problem: Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

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


class Solution(object):

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        sum = 0
        if root is None:
            return 0

        if low <= root.val <= high:
            sum += root.val

        if low < root.val:
            sum += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            sum += self.rangeSumBST(root.right, low, high)

        return sum


def construct_bst(elements):
    tree = TreeNode(elements[0])
    for e in elements:
        tree.add_child(e)

    return tree


if __name__ == "__main__":
    root = [10, 5, 15, 3, 7, 18]
    tree = construct_bst(elements=root)
    solution = Solution()
    solution.rangeSumBST(root=tree, low=7, high=15)
