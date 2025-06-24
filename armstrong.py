num = int(input("Enter a number: "))
sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))

if num == sum_of_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
