while True:
    how_fall_1 = 0
    how_fall_2 = 0
    player_time_1 = 0
    player_time_2 = 0
    for i in range(24):
        command = int(input("введите номер команды (1/2):"))
        if command == 1:
            how_fall_1 += 1
            player_time_1 += int(input(f"введите на сколько времени отстранили игрока №{i}:"))
        elif command == 2:
            how_fall_2 += 1
            player_time_2 += int(input("введите на сколько времени отстранили игрока №{i}:"))
        
    print(f"в комманде 1 было {how_fall_1} удалений играков в сумме на {player_time_1} минут")
    print(f"в комманде 2 было {how_fall_2} удалений играков в сумме на {player_time_2} минут")
        
