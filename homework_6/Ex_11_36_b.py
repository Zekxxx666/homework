import random

my_collection = []

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 1000))

print(f"изначальный массив {my_collection}")

print("вся часть массива не привышающая 100:")
for i in range(counts_elements):
    if my_collection[i] <= 100:
        print(my_collection[i], end= ", ")



