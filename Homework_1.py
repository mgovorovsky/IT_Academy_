text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. " \
    "А у нас управдом — друг человека!"
print ("Шаг 1. Количество символов в строке -",len(text))
print ("Шаг 2. Результат разворота строки:",text[::-1])
print ("Шаг 3. Строка со всеми первыми прописными буквами:",text.title())
print ("Шаг 4. Строка со всеми прописными буквами:",text.upper())
a = text.count('нд')
b = text.count('ам')
c = text.count('о')
print ("Шаг 5. Числов вхождений \"нд\", \"ам\", \"о\" в строку:",a,",",b,",",c)
print ("Шаг 6. Строка со всеми строчными буквами:",text.lower())
c=text.split()
d=c[::-1]
print("Шаг 7. Сложный разворот строки:"," ".join(d))
print ("Шаг 8. Исходная строка:",text)