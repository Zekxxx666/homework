while True:
    arrow_tilt = int(input("введите на сколько градусов повернулась стрелка:"))
    result = []

    if arrow_tilt < 0 or arrow_tilt > 360:
        print("число должно быть в диапазоне от 0 до 360")
        continue
    
    result.append(arrow_tilt // 30)
    result.append((arrow_tilt % 30) * 2)

    print("сейчас:")
    print(f"{result[0]} часов {result[1]} минут")

    result.clear