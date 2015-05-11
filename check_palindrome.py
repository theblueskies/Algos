__author__ = 'blade'

def palindrome():
    data = "16461"
    stacker = []
    for a in data:
        stacker.append(a)

    reverse = []
    while stacker:
        reverse.append(stacker.pop())

    if "".join(reverse) == data:
        print "Palindrome"

    print "".join(reverse)

palindrome()