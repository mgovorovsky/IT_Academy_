print("Введите Ваш вес в кг.:")
a = int(input())
print("Введите Ваш рост в см.:")
b = int(input())
index = a / (b/100 * b/100)
weight_index = round(index, 1)
x = 15
y = 45
steps = 18
step = ((y - x) / steps)
position1 = round((weight_index - x) / step)
item1 = '='
result1 = (str(x),item1 * position1,'|',item1 * (steps - position1),str(y))
print("Ваш индекс массы тела:", weight_index)
print("".join(result1))