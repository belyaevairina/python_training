#При заданном целом трехзначном числе n посчитайте n + nn + nnn:\
x = int(input())

print(x + (x * x) + (x * x * x))

#Сложите цифры целого числа
x = input()

print(sum(map(int,x)))

#Найти корень третьей степени из 343:
print(343**(1/3))
#из любого числа:
x = int(input())

print(x**(1/3))

#В строке удалить все буквы "а" и подсчитать количество удаленных символов:
x = str(input())

print(x.count("a"))
print(x.replace("a", ""))

#Написать произвольную анкету и вывести полученные данные:
first_name = input()
last_name = input()
gender = input()
age = input()
city = input()

print(f'Имя:{first_name} Фамилия:{last_name} Пол:{gender} Возраст:{age} Город:{city}')

#Проверить, что номера телефонов состоят только из цифр. Они могут начинаться с "+",
#цифры могут разделяться пробелами и дефисами:
row_number = str(input())

number2 = row_number.replace("+", "")
number1 = number2.replace(" ", "")
number = number1.replace("-", "")

print(number.isdigit())

#Посчитать количество слов в строке:
x = input()

x = x.split()
y = len(x)

print(y)

#Дана строка содержащая полное имя файла,
# например, С:\development\inside\test-project_management\inside\myfile.txt
# Выделите из этой строки имя файла без расширения:
full_name = 'С:\development\inside\test-project_management\inside\myfile.txt'


name2 = full_name.split("\\")
name1 = name2[-1]
name = name1.split(".")

print(name[0])
