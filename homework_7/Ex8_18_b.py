while True:
    parallel_number = 0
    parallel_number_copy = 0
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

            parallel_number += class_

            if parallel_number > parallel_number_copy:
                parallel_number_copy = parallel_number
        parallel_number = 0


            
