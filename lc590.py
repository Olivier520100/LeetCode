"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        a = []
        def order(node: 'Node', aret) ->List[int]:
            if node != None:
                
                if node.children != None:
                    i = 0
                    while (i < len(node.children)):
                        aret = order(node.children[i],aret)
                        i+=1
                aret.append(node.val)

            
                
            return aret

        a = order(root, a)
        

        return a