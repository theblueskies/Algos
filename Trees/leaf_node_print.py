from level_wise_insert import Tree
from node import Node


class LeafNodePrint(Tree):
    def print_leaf_nodes(self, current_node):
        if current_node == None:
            return
        else:
            if not (current_node.left_child or current_node.right_child):
                current_node.print_node()
            if current_node.left_child:
                self.print_leaf_nodes(current_node=current_node.left_child)
            if current_node.right_child:
                self.print_leaf_nodes(current_node=current_node.right_child)


if __name__ == "__main__":
    tree_instance = LeafNodePrint()
    tree_instance.level_wise_insert([1,2,3,4,5,6,7,8,9])
    tree_instance.print_leaf_nodes(tree_instance.root)
