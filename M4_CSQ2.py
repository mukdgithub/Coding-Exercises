''' M4_CSQ2 MODULE 4 _ CYCLE SHEET 
	Construct a python program to implement reverse polish notation calculator
    In reverse polish notation, mathematical expressions are written
    with the operator following its operands. For example, 3 + 4 becomes 3 4 +.
    Order of operations is entirely based on the ordering of the operators
    and operands. To write 3 + (4 ∗ 2), we would write 3 4 2 ∗ + in RPN.
    The expressions are evaluated from left to right.
    Evaluate the expression and display the result.     '''

n = int(input())
lst = input().split()
stack = []
for i in lst:
    if (i == '+'):
        stack[-2] = stack[-2] + stack[-1]
        stack.pop()
    elif (i == '-'):
        stack[-2] = stack[-2] - stack[-1]
        stack.pop()
    elif (i == '*'):
        stack[-2] = stack[-2] * stack[-1]
        stack.pop()
    elif (i == '/'):
        stack[-2] = stack[-2] / stack[-1]
        stack.pop()
    else:
        stack.append(int(i))
print(int(stack[0]))
print('21BCI0003')
print('MUKUND AGARWAL')
# end of program