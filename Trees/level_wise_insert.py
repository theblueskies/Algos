class Node(object):
    def __init__(self, value=None):
        self.key = value
        self.left_child = None
        self.right_child = None

class Tree(object):
    def __init__(self):
        self.root = None

    def level_wise_insert(self, array):
        queue = []
        if len(array) and self.root == None:
            element = array.pop(0)
            self.root = Node(element)

        # The queue keeps track of the nodes in a level
        queue.append(self.root)
        current_node = None

        while len(array):
            if current_node == None:
                current_node = queue.pop(0)
            element = array.pop(0)

            # If both the children of the current_node have been filled,
            # get the next node from the queue.
            if current_node.left_child and current_node.right_child:
                current_node = queue.pop(0)

            # This next if elif block fills the children of a given node, before
            # moving on to the next node in the same level
            if current_node.left_child == None:
                current_node.left_child = Node(element)
                # Append the newly made node into the queue
                queue.append(current_node.left_child)

            elif current_node.right_child == None:
                current_node.right_child = Node(element)
                # Append the newly made node into the queue
                queue.append(current_node.right_child)

    def level_wise_print(self):
        queue = []
        queue.append(self.root)
        while queue:
            current_node = queue.pop(0)
            print (current_node.key, end=' ')
            if current_node.left_child:
                queue.append(current_node.left_child)
            if current_node.right_child:
                queue.append(current_node.right_child)


instance = Tree()
instance.level_wise_insert([1,2,3,4,5,6,7,8,9])
instance.level_wise_print()
