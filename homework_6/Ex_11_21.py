import random

result = 0
my_collection = []

counts_elements = 31

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 100))

for i in range(counts_elements):
    result += my_collection[i]
print(f"сумма осадков = {result}")