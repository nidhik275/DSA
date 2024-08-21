# Reference: https://medium.com/@sergioli/breath-first-and-depth-first-search-on-tree-and-graph-in-python-99fd1861893e
# doc 2: https://llego.dev/posts/implementing-depth-first-search-python-traverse-binary-tree/ 
# doc 3: https://www.youtube.com/watch?v=fAAZixBzIAI&t=2152s

class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None
'''
class Solution: 
    def dfs(self, root):
        dfs_output = []
        temp_stack = []
        if not root:
            return None
        
        if not root.left and not root.right:
            return root.value

        temp_stack.append(root)
        
        while temp_stack:
            temp = temp_stack.pop()
            value = dfs_output.append(temp.value)            
            if temp.right:
                temp_stack.append(temp.right)
            if temp.left: 
                temp_stack.append(temp.left)

        return dfs_output
'''

#recursive 

class Solution:
    def dfsRecursive(self, root):
        if not root:
            return

        print(root.value, end='')
        self.dfsRecursive(root.left)     
        self.dfsRecursive(root.right)  
             
               
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

solution = Solution()
#output = solution.dfs(root)

solution.dfsRecursive(root)

                