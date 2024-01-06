def evaluate_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

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

    # Iterate through the expression in reverse order
    for char in reversed(expression):
        if char.isdigit():
            # If the character is a digit, push it onto the stack
            stack.append(int(char))
        elif char in operators:
            # If the character is an operator, pop two operands from the stack,
            # perform the operation, and push the result back onto the stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = apply_operator(char, operand1, operand2)
            stack.append(result)

    # The final result is at the top of the stack
    return stack[0]

# Example usage:
prefix_expression = "*+42-75"
result = evaluate_prefix(prefix_expression)
print(f"The result of the prefix expression {prefix_expression} is: {result}") # 12
