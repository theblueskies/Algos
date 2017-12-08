from level_wise_insert import Tree
from node import Node


# Check if tree2 is in tree1
def check_subtree(tree1, tree2):
    if tree2 == None:
        return True
    if tree1 == None:
        return False

    if tree1.key == tree2.key:
        if is_identical(tree1, tree2):
            return True

    return check_subtree(tree1.left_child, tree2) or check_subtree(tree1.right_child, tree2)


def is_identical(tree1, tree2):
    if tree2 == None:
        return True
    if tree1.key != tree2.key:
        return False
    result = is_identical(tree1.left_child, tree2.left_child) and \
             is_identical(tree1.right_child, tree1.right_child)
    return result


if __name__ == "__main__":
    tree_1 = Tree()
    tree_1.level_wise_insert([1,2,3,4,5,6,7,8,9])

    tree_2 = Tree()
    tree_2.level_wise_insert([3,6])

    print(check_subtree(tree_1.root, tree_2.root))
