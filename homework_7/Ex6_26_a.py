while True:
    number = int(input("введите число:"))
    digit = 0
    digit_2 = 0

    if number < 0:
        number *= -1
    
    while number > 0:
        digit = number % 10
        if digit > digit_2:
            digit_2 = digit
        number = number // 10

    print(f"самая большая цифра в вашем числе это: {digit_2}")
