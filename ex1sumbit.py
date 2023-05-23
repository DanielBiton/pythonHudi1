number = int(input("Enter a number: "))

print(f'Complete parts of {number}: ')

for i in range(1, number):
    if number % i == 0:
        print(i)

print(number)