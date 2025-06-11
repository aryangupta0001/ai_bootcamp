operators = ['+', '-', '*', '/']

result = ''


while True:
    exp = input()

    expression = str(result) + exp

    for i in range(len(expression)):
        if(expression[i] in operators):
            operator = expression[i]
            operands = expression.split(operator)
            break
        
    if('.' in operands[0]):
        a = float(operands[0])
    
    else:
        a = int(operands[0])
        
    
    
    if('.' in operands[1]):
        b = float(operands[1])
    
    else:
        b = int(operands[1])



    match operator:
        case '+':
            result = a+b
        
        case '-':
            result = a-b
        
        case '*':
            result = a*b
        
        case '/':
            result = a/b
        
    print(result, end = '')