def infix_to_postfix(infix_expression):
    # Dictionary to store operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(char):
        return char in precedence

    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    postfix_result = []  # List to store the postfix expression
    operator_stack = []  # Stack to store operators

    for char in infix_expression:
        if char.isalnum():
            # If the character is an operand, add it to the result
            postfix_result.append(char)
        elif char == '(':
            # If the character is an opening parenthesis, push it onto the stack
            operator_stack.append(char)
        elif char == ')':
            # If the character is a closing parenthesis, pop operators from the stack
            # and add them to the result until an opening parenthesis is encountered
            while operator_stack and operator_stack[-1] != '(':
                postfix_result.append(operator_stack.pop())
            operator_stack.pop()  # Pop the opening parenthesis
        elif is_operator(char):
            # If the character is an operator, pop operators from the stack
            # and add them to the result as long as they have higher or equal precedence
            while operator_stack and has_higher_precedence(operator_stack[-1], char):
                postfix_result.append(operator_stack.pop())
            operator_stack.append(char)

    # Pop any remaining operators from the stack and add them to the result
    while operator_stack:
        postfix_result.append(operator_stack.pop())

    # Convert the result list to a string
    return ''.join(postfix_result)

# Example usage:
infix_expression = "2 + 3 * 4"
postfix_expression = infix_to_postfix(infix_expression)
print(f"The postfix expression for {infix_expression} is: {postfix_expression}")
