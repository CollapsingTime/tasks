def check_brackets(input_line):
    stack = []
    temp = {'(': ')', '[': ']', '{': '}'}
    for i in input_line:
        if len(input_line) % 2 == 1:
            return False
        elif i in '([{':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            left = stack.pop()
            right = temp[left]
            if right != i:
                return False
    return len(stack) == 0
          
print(check_brackets('()[]{}'))  # True
print(check_brackets('(]'))  # False
print(check_brackets('(('))  # False
print(check_brackets(''))  # True