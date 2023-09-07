"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа: n — кол-во элементов первого множества,
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
dataset_1 = []
dataset_2 = []
for i in range(n):
    dataset_1.append(int(input(f"Введите {i+1} элемент первого множества: ")))
for i in range(m):
    dataset_2.append(int(input(f"Введите {i+1} элемент второго множества: ")))
dataset_1 = set(dataset_1)
dataset_2 = set(dataset_2)
result_set = list(dataset_1.intersection(dataset_2))
for i in range(len(result_set) - 1):
    for j in range(i + 1, len(result_set)):
        if result_set[j] < result_set[i]:
            result_set[i], result_set[j] = result_set[j], result_set[i]
print(result_set)
