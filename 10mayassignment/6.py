def is_perfect(number):
    if number <= 0:
        return False
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number
num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")

