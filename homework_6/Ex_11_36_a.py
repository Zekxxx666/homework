import random

my_collection = []

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(-100, 100))

print(f"изначальный массив {my_collection}")

print("неотрецательная часть массива:")
for i in range(counts_elements):
    if my_collection[i] > 0:
        print(my_collection[i], end= ", ")


