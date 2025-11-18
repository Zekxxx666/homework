import random

my_collection = []
result = 0

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 100))

print(f"изначальный массив {my_collection}")

print("сумма каждого 2 числа:")
for i in range(0, counts_elements, 2):
    result += my_collection[i]

print(result)
