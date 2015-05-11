__author__ = 'blade'

import sys

###linkedlist




class node(object):

    def __init__(self):
        self.data=None
        self.next=None

class linked_list:
    def __init__(self):
        self.heado=None

    def something(self):
        print ("something")

    def robtraverse(self):
        taxi = node()
        taxi = self.heado
        while (taxi.next is not None):
            taxi = taxi.next
        return taxi

    def add_node(self, data):
        new_node = node()
        new_node.data = data
        #new_node.next = self.heado
        #self.heado = new_node

        if self.heado is None:
            self.heado = new_node
            new_node.next = None
        else:
            t = node()
            t.next = self.heado
            while t.next is not None:
                t = t.next
            t.next = new_node
            new_node.next=None


    def print_list(self):
        bnode=node()
        bnode=self.heado
        while bnode:
            print 'Data ', bnode.data
            bnode = bnode.next


if __name__=='__main__':
    linko = linked_list()
    linko.add_node(4)
    linko.add_node(3)
    linko.add_node(2)
    linko.add_node(1)
    linko.print_list()


