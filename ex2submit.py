count = 1
total = 0

while True:
    number = int(input(f"Please enter number : # {count} : "))

    if number < 0:
        break

    total = total + number
    average = total / count

    print(f" avg={average}. (sum={total}) ")

    count = count + 1

print("goodbye. thank you!")
