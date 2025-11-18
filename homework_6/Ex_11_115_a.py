import random

my_collection = []
max_speed_car = 0
end_i = []

counts_elements = 40

for _ in range(counts_elements):
    my_collection.append(random.randint(100, 400))

print(f"изначальный массив {my_collection}")

for i in range(counts_elements):
    if my_collection[i] > max_speed_car:
        end_i.clear()
        max_speed_car = my_collection[i]
        end_i.append(i)
    elif my_collection[i] == max_speed_car:
        end_i.append(i)

print(f"самая быстрая машина (первая из списка) №{end_i[0]} с скоростью {max_speed_car}")



