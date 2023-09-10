class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def top_view(root):
    def dfs(node, distance, level):
        if not node:
            return
        
        if distance not in horizontal_distance:
            horizontal_distance[distance] = (node.info, level)
            print(f'horizontal_distance {horizontal_distance}')
        elif level < horizontal_distance[distance][1]:
            horizontal_distance[distance] = (node.info, level)
            print(f'horizontal_distance {horizontal_distance}')

        dfs(node.left, distance-1, level + 1)
        dfs(node.right, distance+1, level+1)    

    if not root:
        return

    horizontal_distance = {}

    dfs(root, 0, 0)    

    sorted_horizontal_distance = sorted(horizontal_distance.items(), key=lambda x: x[0])
    for distance, (value, level) in sorted_horizontal_distance:
        print(value, end=' ')



root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(6)
root.right.right.left.right = TreeNode(4)

print(top_view(root))