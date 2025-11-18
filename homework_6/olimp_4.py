r_ogorod = int(input("введите радиус огорода:"))
r_krug_1 = int(input("введите радиус 1 круга:"))
r_krug_2 = int(input("введите радиус 2 круга:"))

if r_ogorod <= r_krug_1 or r_ogorod <= r_krug_2:
    print("NO")
else:
    print("YES")