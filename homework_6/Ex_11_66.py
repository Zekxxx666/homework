import random

my_collection = []
result = 0

counts_elements = 25

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 5))

print(f"изначальный массив {my_collection}")

print("числа массива не прывышающие 20:")
for i in range(counts_elements):
    if my_collection[i] <= 2:
        result += 1

print(f"количество неуспевающих учеников: {result}")


