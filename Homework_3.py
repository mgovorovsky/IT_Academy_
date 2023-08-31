print("Введите значение 1:") 
a = int(input())
print("Введите значение 2:") 
b = int(input())
print("Введите значение 3:") 
c = int(input())
step_1 = a != 0 and b != 0 and c != 0 and "Нет нулевых значений!!!"
print(step_1)
step_2 = 0 or a or b or c or "Введены все нули!"
print(step_2)
if a > (b + c):
    print(a - b - c)
if a < (b + c):
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print("Вася")
if a > 5 or (b == 7 and c  == 7):
    print("Петя")