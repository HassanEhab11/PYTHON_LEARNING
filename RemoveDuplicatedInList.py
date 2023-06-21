numbers = [2, 10, 20, 25, 87, 10, 10, 10, 20, 25]
numbers0 = []
for number in numbers:
    if number not in numbers0:
        numbers0.append(number)

print(numbers0)
