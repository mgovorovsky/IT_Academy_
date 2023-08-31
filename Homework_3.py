print("Введите значение 1:") 
a = int(input())
print("Введите значение 2:") 
b = int(input())
print("Введите значение 3:") 
c = int(input())
step_1 = a and b and c and "Нет нулевых значений!!!"
print('step1', step_1)
step_2 = a or b or c or "Введены все нули!"
print('step2', step_2)
if a > (b + c):
    print(a - b - c)
if a < (b + c):
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print("Вася")
if a > 5 or (b == 7 and c  == 7):
    print("Петя")