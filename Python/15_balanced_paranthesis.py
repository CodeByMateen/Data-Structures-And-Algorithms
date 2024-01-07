def are_parentheses_balanced(expression):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return not stack

# Example usage:
expression = "(({}))"
result = are_parentheses_balanced(expression)

if result:
    print(f"The parentheses in the expression '{expression}' are balanced.")
else:
    print(f"The parentheses in the expression '{expression}' are not balanced.")
