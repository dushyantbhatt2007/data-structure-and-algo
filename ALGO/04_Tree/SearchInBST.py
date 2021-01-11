class TreeNode():
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
    def searchBST(self, root, val):
        if val == root.val:
            return root

        if val < root.val and root.left:
            return self.searchBST(root=root.left, val=val)

        if val > root.val and root.right:
            return self.searchBST(root=root.right, val=val)


    def searchBST1(self, root, val):
        while root:
            if val == root.val:
                return root
            if val < root.val:
                if root.left:
                    root = root.left
                else:
                    return None
            else:
                if root.right:
                    root = root.right
                else:
                    return None




def construct_BST(elements):
    tree = TreeNode(elements[0])
    for e in elements:
        tree.add_child(e)
    return tree


if __name__ == "__main__":
    elements = [4, 2, 7, 1, 3]
    tree = construct_BST(elements=elements)
    solution = Solution()
    output = solution.searchBST(root=tree, val=2)
    output = solution.searchBST1(root=tree, val=2)
    pass