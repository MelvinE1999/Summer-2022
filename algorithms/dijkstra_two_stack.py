# operand stack and operator stack
# must follow PEMDAS
# open parenthesis push on operand 
# when close found pop till get to open
# always pop two off of the stack
# end of program final output is on the operand stack



def dijkstraTwoStack(equation:str) -> float:
    operandStack = []
    operatorStack = []

    lowOperators = ["+","-"]
    highOperators = ["/","*"]
    for token in equation:
        if token == ' ':
            continue
        elif token == "(":
            operatorStack.append("(")
        elif token in lowOperators: 
            if operatorStack[len(operatorStack) - 1] in highOperators: # here to hold pemdas as true
                num2 = operandStack.pop()
                num1 = operandStack.pop()
                operandStack.append(calculate(operatorStack.pop(), num1, num2))
            operatorStack.append(token)
        elif token in highOperators:
            operatorStack.append(token)
        elif token == ")":
            while operatorStack[len(operatorStack) - 1] != "(":
                num2 = operandStack.pop()
                num1 = operandStack.pop()
                operandStack.append(calculate(operatorStack.pop(), num1, num2))
            _ = operatorStack.pop()
        else: # adds numbers to operand stack
            operandStack.append(float(token))
   
    # checks for tailing numbers
    while len(operatorStack) != 0:
        num2 = operandStack.pop()
        num1 = operandStack.pop()
        operandStack.append(calculate(operatorStack.pop(), num1, num2))

    return operandStack.pop()


def calculate(operator:str , num1:float, num2:float) -> float:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 / num2
    else:
        return num1 * num2

def tester():
    assert dijkstraTwoStack("2 * (3 + 4) - 5") == 9.0
    assert dijkstraTwoStack("(2 / 4) * 2 + 2 - 2") == 1.0


if __name__ == "__main__":
    tester()