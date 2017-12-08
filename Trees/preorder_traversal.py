from level_wise_insert import Tree
from node import Node


def preorder_traversal(node):
    if node != None:
        print(node.key)
        preorder_traversal(node.left_child)
        preorder_traversal(node.right_child)



if __name__ == "__main__":
    tree = Tree()
    tree.level_wise_insert([1,2,3,4,5,6,7,8,9])

    preorder_traversal(tree.root)
