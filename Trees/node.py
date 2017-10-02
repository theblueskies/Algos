import sys


class Node(object):
    def __init__(self, value=None):
        self.key = value
        self.left_child = None
        self.right_child = None

    def print_node(self):
        if sys.version_info[0] == 3:
            print (self.key, end=' ')
        else:
            raise 'Only supports python3 for print'
