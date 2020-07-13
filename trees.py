# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def height(self,node):
        if node is None:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        if left > right:
            return self.height(left) + 1
        if right > left:
            return self.height(right) + 1


    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0

        if root is None:
            return sum

        if L <= root.val <= R:
            sum = sum + root.val

        if root.val >= L:
            sum = sum + self.rangeSumBST(root.left, L, R)

        if root.val <= R:
            sum = sum + self.rangeSumBST(root.right, L, R)

        return sum

    def inorderTraversal(self, root: TreeNode):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res


    def preorderTraversal(self, root: TreeNode):
        res = []
        if root:
            res.append(root.val)
            res = self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
        return res


    def postorderTraversal(self, root: TreeNode):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
            res.append(root.val)
        return res

    def auxD(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(1 + self.auxD(root.left), 1 + self.auxD(root.right))

    def depthBfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        c = 1
        # storing size is a good optimisation
        # do this more regularly
        size = 1
        while q:
            for _ in range(size):
                popped = q.popleft()
                # ensure null checks are good
                # these can trip up
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            size = len(q)
            # Be careful when to add 1 to the size
            # Prevent the last one from being added
            # Or just subtract 1
            if size > 0:
                c += 1
        #     c += 1
        #
        # return c - 1
        return c



    def qD(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        c, n = 1, 1
        while q:
            for _ in range(n):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            n = len(q)
            if n != 0:
                c += 1
        return c

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.auxD(root)


    def size_of_tree(self,root):
        if root is None:
            return 0
        else:
            return self.size_of_tree(root.left) + 1 + self.size_of_tree(root.right)


    def isSameTree(self, p, q):

        p = self.bst(p)
        q = self.bst(q)

        print(p)
        print(q)

        return p == q

    def bst(self, root):

        output = deque()
        output.append(root)

        return_list = []

        level = 1
        while output:
            for _ in range(level):
                curr = output.pop()
                if curr:
                    return_list.append(curr.val)
                    output.append(curr.left)
                    output.append(curr.right)
                else:
                    return_list.append(None)
            level = len(output)
        return return_list

    def isSameTree_efficient(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

    def isPalindrome(self, x):
        i = 0
        j = len(x) - 1

        while i != j or i < len(x) or j > 0:

            if i == j:
                return True
            if x[i] != x[j]:
                return False
            i += 1
            if i == j:
                return True
            j -= 1




