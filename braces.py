closing_brace_match = {'{': '}', '[': ']', '(': ')'}
open_braces = ['{', '[', '(']

def braces(values):
    output_array = []
    for item in values:
        check = check_braces(item)
        output_array.append(check)
    return output_array

def check_braces(brace_string):
    parentheses_stack = []
    for brace in brace_string:
        if len(parentheses_stack):
            last_brace = parentheses_stack[-1]
            if brace in open_braces:
                parentheses_stack.append(brace)
            else:
                if brace == closing_brace_match[last_brace]:
                    parentheses_stack.pop()
        else:
            parentheses_stack.append(brace)

    if len(parentheses_stack) != 0:
        parentheses_stack=[]
        return "NO"
    return "YES"
