from level_wise_insert import Tree
from node import Node


def postorder_traversal(node):
    if node != None:
        postorder_traversal(node.left_child)
        postorder_traversal(node.right_child)
        print(node.key)
    return



if __name__ == "__main__":
    tree = Tree()
    tree.level_wise_insert([1,2,3,4,5,6,7,8,9])

    postorder_traversal(tree.root)
