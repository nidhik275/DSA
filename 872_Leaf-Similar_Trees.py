from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def countLeaves(root):
            leaves = []
            stack = [root]
            while stack:
                temp = stack.pop()
                if not temp.right and not temp.left: 
                    leaves.append(temp.value)
                    
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
            return leaves
        output1 = countLeaves(root1)    
        output2 = countLeaves(root2)
        if output1 == output2:
            return True
        else:
            return False

#optimised 2 - less space complexity
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        output1, output2 = [], []
        def countLeaves(root):
            leaves = []
            stack = [root]
            while stack:
                temp = stack.pop()
                if not temp.right and not temp.left: 
                    leaves.append(temp.val)
                    
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
            return leaves
        
        return countLeaves(root1) == countLeaves(root2)


'''

#optimsation 3 with recursion

'''

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(root):                              #     Example: 
                                                    #         root1:         root2:
                                                    #            ______3__             __3__
                                                    #           /         \           /     \
                                                    #          5__         1         5       1__
                                                    #         /   \       / \       / \     /   \
                                                    #       *6*    2    *9* *8*   *6* *7* *4*    2
                                                    #             / \                           / \
                                                    #           *7* *4*                       *9* *8*
                                                    #   root1:
            if not root: return []                  #       node      dfs(root.left)+dfs(root.right)
                                                    #       ––––      ––––––––––––––––––––––––––––––
            if not root.left and not root.right:    #        2              [7] + [4]   = [7,4]
                return [root.val]                   #        5              [6] + [7,4] = [6,7,4]
                                                    #        1              [9] + [8]   = [9,8]
            return dfs(root.left) + dfs(root.right) #        3          [6,7,4] + [9,8] = [6,7,4,9,8] <--
                                                    #
        return dfs(root1) == dfs(root2)             #   root2:
                                                    #       node      dfs(root.left)+dfs(root.right)
                                                    #       ––––      ––––––––––––––––––––––––––––––
                                                    #        5            [6] + [7]     = [6,7]
                                                    #        2            [9] + [8]     = [9,8]
                                                    #        1            [4] + [9,8]   = [4,9,8]
                                                    #        3          [6,7] + [4,9,8] = [6,7,4,9,8] <--

                                                    #       Return True


'''


        