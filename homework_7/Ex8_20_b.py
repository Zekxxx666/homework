import numpy as np
while True:
    result = 0
    doxod = []
    doxod_1 = []
    for i in range(1, 3 + 1):
        doxod = list(map(int, input(f"введите зарплату за 10 дней {i} магазина:").split()))
        
        doxod_1 = np.copy(doxod)
        print(doxod_1)


            