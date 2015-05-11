from codes import linked_list
from codes import node
a = linked_list()
b = linked_list()

a.add_node(-2)
a.add_node(0)
a.add_node(2)
a.add_node(4)

b.add_node(1)
b.add_node(3)
b.add_node(5)

def linklength(a):
    curr = a.heado
    count = 0
    while curr is not None:
        count+=1
        curr=curr.next
    return count

def mergelink(a,b):
    length_a = linklength(a)
    length_b = linklength(b)
    if length_a > length_b:
        c = mergeo(a,b)
    else:
        c = mergeo(b,a)
    c.print_list()
    return c

def mergeo(a,b):
    c = linked_list()
    a = a.heado
    b = b.heado
    while a!=None and b!=None:
        if a.data<=b.data:
            c.add_node(a.data)
            a = a.next
        else:
            c.add_node(b.data)
            b=b.next
    while a is not None:
        c.add_node(a.data)
        a = a.next
    while b is not None:
        c.add_node(b.data)
        b=b.next
    return c

def reverse(lista):
    if lista is None:
        return
    reverse(lista.next)
    print lista.data


data = mergelink(a,b)
print "\n\nReverse:  "
reverse(data.heado)