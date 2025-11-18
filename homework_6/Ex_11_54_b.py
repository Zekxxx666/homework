import random

my_collection = []
number = int(input("введите число а:"))

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 100))

print(f"изначальный массив {my_collection}")

print(f"числа массива не прывышающие {number}:")
for i in range(counts_elements):
    if my_collection[i] <= number:
        print(my_collection[i], end= ", ")


