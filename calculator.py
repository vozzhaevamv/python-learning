def calculator(operator,value1, value2):
    if operator == '+' :
        print (value1 + value2)
    elif operator == '-':
        print (value1 - value2)
    elif operator == '*' :
        print (value1 * value2)
    elif operator == '/':
        print (value1 / value2)
while True:
        operator = str(input("оператор: "))
        if operator == 'стоп':
            break
        value1 = int(input("Введите первое значение: "))
        value2 = int(input("Введите второе знчение: "))
        calculator(operator, value1, value2)




