import string

mapping = {}
for letter in string.ascii_uppercase:
    mapping[ord(letter) - 64] = letter

def solution(string_sequence, current_path='', all_paths=[]):
    # if len(string) == 0, we have successfully decoded entire string. It can
    # now be added to the all_paths, which hosts list of all decoded strings.
    if len(string_sequence) == 0:
        all_paths.append(current_path)
        return ''

    else:
        if len(string_sequence) == 1:
            key_list = [string_sequence[0]]
        elif len(string_sequence) > 1:
            key_list = [string_sequence[:2], string_sequence[0]]

        for key in key_list:
            if int(key) <= 26:
                copy_of_path = current_path
                current_path += mapping[int(key)]
                new_path = solution(string_sequence[len(key):], current_path)
                current_path = copy_of_path # Re-initialize current_path to the copy before recursion
    return all_paths


result = solution(string_sequence='121')
print(result)
