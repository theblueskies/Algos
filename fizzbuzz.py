def fizzbuzz(upper_bound):
    """
    if n is divisible by 3 print fizz
    if n is divisible by 5 print buzz
    if n is divisible by 3 and 5 print fizzbuzz
    for all numbers less than and including n

    parameters: n - an integer
    """
    fizzbuzz_list = range(upper_bound+1)
    for n in fizzbuzz_list:
        if n>0:
            if n%3==0 and n%5==0:
                print("fizzbuzz: {}".format(n))
            elif n%3==0:
                print("fizz: {}".format(n))
            elif n%5==0:
                print("buzz: {}".format(n))


if __name__ == '__main__':
    fizzbuzz(20)