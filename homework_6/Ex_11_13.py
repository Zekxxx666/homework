import random

index_collection = 0
my_collection = []

counts_elements = 10

for _ in range(counts_elements):
    my_collection.append(random.randint(1, 100))

index_collection = int(input("введите индекс числа массива что-бы узнать его значение:"))

print(f"число пд индексом {index_collection} = {my_collection[index_collection]}")