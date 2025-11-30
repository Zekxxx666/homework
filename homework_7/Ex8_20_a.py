while True:
    result = 0
    zarplata = 0
    for i in range(1, 3 + 1):
        for j in range(1, 10 + 1):                                           
            class_ = int(input(f"введите зарплату  {i} магазина {J} день:"))

            zarplata += class_

            if zarplata > result:
                result = zarplata
        zarplata = 0