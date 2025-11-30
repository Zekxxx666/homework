while True:
    class_a = 0
    class_b = 0
    class_c = 0
    class_d = 0
    result = 0
    for i in range(1, 11 + 1):
        for j in range(1, 4 + 1):
            if j == 1:
                parallel = "A"
            elif j == 2:
                parallel = "Б"
            elif j == 3:
                parallel = "В"
            elif j == 4:
                parallel = "Г"                                             
            class_ = int(input(f"введите количество учеников в {i}{parallel} классе  "))

            if j == 1:
                class_a += class_
            elif j == 2:
                class_b += class_
            elif j == 3:
                class_c += class_
            else:
                class_d += class_
    
    class_abcd = [class_a, class_b, class_c, class_d]
    sorted(class_abcd)
    print(f"{class_abcd[0]}- минимальное количество учеников в 1 паралели")
