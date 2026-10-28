def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


try:
    value = int(input("Enter an integer: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if is_prime(value):
        print(f"{value} is prime.")
    else:
        print(f"{value} is not prime.")
