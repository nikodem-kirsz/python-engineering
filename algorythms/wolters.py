class Node:
    def __init__(self, name, children=None):
        self.__name = name
        if children is None:
            self.__children = []
        else:
            self.__children = children
 
    def add_child(self, node):
        self.children.append(node)
 
    @property
    def children(self):
        return self.children[:]

     



    # TODO: -> please write below a method that will take a node (for instance the root) of the tree and will count all elements belong to it (including the root node)
    def count(root: 'Node') -> int:
        count = 0
        stack = [root] # 
        count += 1

        while len(stack):
            current_node = stack.pop(0) 
            for node in current_node.children:
                stack.append(node)
                count += 1      

        return count
 
def count(root: 'Node') -> int:
   count = 1
       
   for node in node.children:
       count += count(node.children)

   return count 


        

           
# {
#    value: 'root',
#    children: [
#        {
#            value: 'child-1',
#            children: [
#                {
#                    value: 'child-1-1'
#                },
#                    value: 'child-1-1'
#                },

#            ]
#        },
#        {
#            value: 'child-2',
#            children: [
#                {
#                    value: 'child-2-1'
#                },
#                {
#                    value: 'child-2-2'
#                }
#            ]
#        }
#    ]
# }
 
 
root = Node('root')
child_1 = Node('child-1')
child_1_1 = Node('child-1-1')
child_2 = Node('child-2')
child_2_1 = Node('child-2-1')
child_2_2 = Node('child-2-2')
 
root.add_child(child_1)
child_1.add_child(child_1_1)
# for children in root.children:
#     print(children)
 
root.add_child(child_2)
child_2.add_child(child_2_1)
child_2.add_child(child_2_1)


 
# should be 6
print(Node.count(root))
