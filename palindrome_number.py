def next_palindrome(number):
    if number == 9:
        return 11
    if number < 9:
        return number+1
    temp = str(number)
    length = len(temp)
    plus = 0
    if temp == temp[::-1]:
        plus = 1
    if length % 2:
        beginning = str(int(temp[:(length/2)+1]) + plus)
        next = int(beginning + beginning[:-1][::-1])
    else:
        beginning = str(int(temp[:length/2]) + plus)
        next = int(beginning + beginning[::-1])
    if next <= number:
        return next_palindrome(next)
    return next

print next_palindrome(1234)