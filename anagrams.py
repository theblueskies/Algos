def anagram(word):
    if len(word) <2:
        return word

    else:
        for i in range(len(word)):
            ana = []
            character = word[i]
            for j in anagram(word[:i] + word[i+1:]):
                print j + character
            # ana.append([anagram(word[:i]),word[i],anagram(word[i+1:])])
            # print (ana)
        # print (''.join(ana))


# anagram('car')

def anagrams(word):
    """ Generate all of the anagrams of a word. """
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            # if not letter in word[:i]: #avoid duplicating earlier words
                for j in anagrams(word[:i]+word[i+1:]):
                    yield j+letter

if __name__ == "__main__":
    for i in anagrams("car"):
        print i
