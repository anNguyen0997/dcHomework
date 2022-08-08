# Write an app which asks users for the input and then prints the factorial for that number.

number = int(input('ENTER A FACTORIAL NUMBER : '))

factorial = 1

for num in range(number, 0, -1):
    factorial *= num

print(factorial)
