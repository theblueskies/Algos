from level_wise_insert import Tree
from node import Node


def inorder_traversal(node):
    if node != None:
        inorder_traversal(node.left_child)
        print(node.key)
        inorder_traversal(node.right_child)
    return



if __name__ == "__main__":
    tree = Tree()
    tree.level_wise_insert([1,2,3,4,5,6,7,8,9])

    inorder_traversal(tree.root)
