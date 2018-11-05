# You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of positive integers.

# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample input:
#     expression1 = "5+16-((9-6)-(4-2))"
#     expression2 = "22+(2-4)"

# Sample output:
#     evaluate(expression1) => 20
#     evaluate(expression2) => 20

# def calculate(input):
#     numbersStack = []
#     operandsStack = []

#     currentNumber = ""
#     for i in range(len(input)-1, -1, -1):
#         if input[i] != "+" and input[i] != "-":
#             currentNumber += input[i]
#         else:
#             numbersStack.append(int(currentNumber[::-1]))
#             operandsStack.append(input[i])
#             currentNumber = ""

#     numbersStack.append(int(currentNumber))

#     while len(operandsStack) > 0:
#         firstNumber = numbersStack.pop()
#         secondNumber = numbersStack.pop()
#         operand = operandsStack.pop()
#         if operand == "+":
#             numbersStack.append(firstNumber + secondNumber)
#         elif operand == "-":
#             numbersStack.append(firstNumber - secondNumber)

#     return numbersStack.pop()

# # expression1 = "6+9-12"
# expression2 = "1+2+3+4-5-6-7"
# print calculate(expression2)





# You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of positive integers.

# We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

# Sample input:
#     expression1 = "5+16-((9-6)-(4-2))"
#     expression2 = "22+(2-4)"

# Sample output:
#     evaluate(expression1) => 20
#     evaluate(expression2) => 20

def calculate(input):
    numbersStack = []
    operandsStack = []

    precedenceNumbersStack = []
    precedenceOperandsStack = []

    currentNumber = ""
    precedenceOperations = False
    for i in range(len(input)-1, -1, -1):
        if input[i] == ")":
            precedenceOperations = True
            precedenceOperandsStack.append(input[i])

        elif input[i] == "(":
            if currentNumber != "":
                precedenceNumbersStack.append(int(currentNumber[::-1]))
                currentNumber = ""
            currentOperator = precedenceOperandsStack.pop()
            while currentOperator != ")":
                firstNumber = precedenceNumbersStack.pop()
                secondNumber = precedenceNumbersStack.pop()
                if currentOperator == "+":
                    precedenceNumbersStack.append(firstNumber + secondNumber)
                elif currentOperator == "-":
                    precedenceNumbersStack.append(firstNumber - secondNumber)
                currentOperator = precedenceOperandsStack.pop()

            if len(precedenceOperandsStack) == 0:
                precedenceOperations = False
                numbersStack.append(precedenceNumbersStack.pop())


        elif input[i] != "+" and input[i] != "-":
            currentNumber += input[i]


        else:
            if precedenceOperations:
                if currentNumber != "":
                    precedenceNumbersStack.append(int(currentNumber[::-1]))
                    currentNumber = ""
                precedenceOperandsStack.append(input[i])
            else:
                if currentNumber != "":
                    numbersStack.append(int(currentNumber[::-1]))
                    currentNumber = ""
                operandsStack.append(input[i])

    numbersStack.append(int(currentNumber))

    while len(operandsStack) > 0:
        firstNumber = numbersStack.pop()
        secondNumber = numbersStack.pop()
        operand = operandsStack.pop()
        if operand == "+":
            numbersStack.append(firstNumber + secondNumber)
        elif operand == "-":
            numbersStack.append(firstNumber - secondNumber)

    return numbersStack.pop()

# expression1 = "6+9-12"
# expression2 = "1+2+3+4-5-6-7"
# print calculate(expression2)


# expression1 = "5+(16-2)"
# expression2 = "5+16-((9-6)-(4-2))"
# expression3 = "22+(2-4)"
expression4 = "1+5-((2-9)-(9-0)+(24-75))+10+(100-9)"
print calculate(expression4)





# expression1 = "6+9-12"
# expression2 = "1+2-3+4-5+6-7" # -2
# expression3 = "1+2+3+4-5-6-7" # -8
# expression4 = "255" # 255
# expression5 = "600+9-12" # 597
# expression6 = "1-2-3-4" # -8

# print calculate("6+9-12")
# print calculate("1+2-3+4-5+6-7")
# print calculate(expression3)
# print calculate(expression4)
# print calculate(expression5)
# print calculate(expression6)
