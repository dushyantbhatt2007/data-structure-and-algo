class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_child(self, val):
        if val == self.val or val is None:
            return

        if val < self.val:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = TreeNode(val)


class Solution:
    def __init__(self):
        self.dummy = TreeNode()
        self.curr = self.dummy

    def increasingBST(self, root: TreeNode)->TreeNode:
        def in_order(root):
            if root:
                in_order(root=root.left)
                self.curr.right = TreeNode(root.val)
                self.curr = self.curr.right
                in_order(root=root.right)
        in_order(root=root)
        return self.dummy.right


def construct_bst(elements):
    tree = TreeNode(elements[0])
    for e in elements:
        tree.add_child(e)
    return tree


if __name__ == "__main__":
    try:
        numbers = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
        tree = construct_bst(elements=numbers)
        solution = Solution()
        output = solution.increasingBST(tree)
    except Exception as ex:
        print(ex)
    pass
