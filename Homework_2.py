print("Введите Ваш вес в кг.:")
a = int(input())
print("Введите Ваш рост в см.:")
b = int(input())
index = a / (b/100 * b/100)
weight_index = round(index, 1)
position1 = round((weight_index - 20) / 1.66)   #18 items between 20 and 50
item1 = '='
result1 = ('20',item1 * position1,'|',item1 * (18 - position1),'50')
print("Ваш индекс массы тела:", weight_index)
print("".join(result1))