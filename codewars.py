n=int(input("Enter a number: "))
def series_sum(n):
    total = []
    for num in range (1,(1+(n - 1) * 3)+1,3):
        total.append(1/num)
    return sum(total)
print(series_sum(n))


def series_sum2(n):
    total2 = 0
    for num in range (1,(1+(n - 1) * 3)+1,3):
        total2 += 1/num
    return  round((total2),2)
print(series_sum2(n))



def series_sum3(n):
    total3 = 0
    for num in range (1,(1+(n - 1) * 3)+1,3):
        total3 += 1/num
    return  f"{total3:.2f}"



##Ваша задача - написать функцию, которая возвращает n-й член следующего ряда, 
# который является суммой первых n членов последовательности (n это входной параметр). 
# ряд чисел 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 