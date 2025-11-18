import random

my_collection = []

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 100))

print(my_collection)

for i in range(1, 10 + 1):
    print(my_collection[-i], end= ", ")