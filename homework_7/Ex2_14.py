while True:
    number = int(input("введите 3-х значное число:"))

    if number < 100 or number > 999:
        print("число 3-х значное")
        continue

    digit_1 = number // 100
    digit_2 = (number // 10) % 10
    digit_3 = number % 10

    number_2 = (digit_2  * 100) + (digit_3 * 10) + (digit_1)

    print(f"полученное число: {number_2}")
 