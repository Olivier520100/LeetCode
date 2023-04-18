

class Solution:


    def preorder(self, root: 'Node') -> List[int]:
        a = []
        def order(node: 'Node', aret) ->List[int]:
            if node != None:
                aret.append(node.val)
                if node.children != None:
                    i = 0
                    while (i < len(node.children)):
                        aret = order(node.children[i],aret)
                        i+=1
                
            return aret

        a = order(root, a)
        

        return a