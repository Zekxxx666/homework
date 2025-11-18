import random

my_collection = []

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 100))

print(f"изначальный массив {my_collection}")

print("числа массива не прывышающие 20:")
for i in range(counts_elements):
    if my_collection[i] <= 20:
        print(my_collection[i], end= ", ")


