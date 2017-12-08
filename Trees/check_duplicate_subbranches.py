from level_wise_insert import Tree
from node import Node


def find_duplicate_subtree(root):
    #d is the set storing hashed subtree
    #lst is the set storing duplicate subtree
    global d, lst
    d = set()
    lst = set()
    def recur(node):
        global d, lst
        # import pdb; pdb.set_trace()
        if not node:
            return ""
        left = recur(node.left_child)
        right = recur(node.right_child)
        hashed = str(node.key) + left + right
        if hashed == '23':
            import pdb; pdb.set_trace()
        if hashed in d:
            lst.add(hashed)
        d.add(hashed)
        return hashed
    recur(root)
    # return [l.split(",") for l in lst]
    return lst


if __name__ == "__main__":
    tree_1 = Tree()
    # tree_1.level_wise_insert([1,2,3,3,5,2,7,2,3,10,2,3])
    tree_1.level_wise_insert([1,2,2,3,1,3,4])
    tree_1.root.left_child.right_child = None
    tree_1.root.right_child.right_child = None

    print(find_duplicate_subtree(tree_1.root))
    # print(d, lst)
