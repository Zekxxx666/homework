
hige_car = 437
hige_most = 0
crash = 0

count_mostov = int(input("введите количество мостов:"))

for i in range(1, count_mostov + 1):
    hige_most = int(input(f"введите высоту {i} моста:"))
    if hige_most >= hige_car:
        crash += 1

print(f"слишком высоких мостов {crash}")
    