def evaluate_postfix(expression):
    stack = []

    # Helper function to perform basic arithmetic operations
    def apply_operator(operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    # Iterate through the expression
    for char in expression:
        if char.isdigit():
            # If the character is a digit, push it onto the stack
            stack.append(int(char))
        else:
            # If the character is an operator, pop two operands from the stack,
            # perform the operation, and push the result back onto the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(char, operand1, operand2)
            stack.append(result)

    # The final result is at the top of the stack
    return stack[0]

# Example usage:
postfix_expression = "46+2/5*7+"
result = evaluate_postfix(postfix_expression)
print(f"The result of the postfix expression {postfix_expression} is: {result}") # 32
