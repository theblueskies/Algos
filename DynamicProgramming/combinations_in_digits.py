'''
Input : 123
Output :1 2 3
        1 23
        12 3
        123

Input : 1234
Output : 1 2 3 4
        1 2 34
        1 23 4
        1 234
        12 3 4
        12 34
        123 4
        1234
'''

def driver(input_string):
    print(input_string)
    print_space_combinations(input_string, input_string)
    print("Set of strings \n", set_of_strings)

set_of_strings = set()

def print_space_combinations(input_string, string_in_memory, index_of_space=1, add_space=True):
    global set_of_strings
    set_of_strings.add(string_in_memory)

    if index_of_space >= len(string_in_memory) or string_in_memory[index_of_space] == '\0':
        return

    copy_of_string_in_memory = string_in_memory
    if string_in_memory[index_of_space] != ' ' and add_space:
        string_in_memory = string_in_memory[:index_of_space] + ' ' + string_in_memory[index_of_space:]
        print(string_in_memory)


    print_space_combinations(input_string, copy_of_string_in_memory, index_of_space+1, add_space=True)
    print_space_combinations(input_string, string_in_memory, index_of_space+2, add_space=True)


if __name__ == "__main__":
    driver('123')
