squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

squares_1 = []
for value in range(1,11):
    squares_1.append(value**2)

print(squares_1)

square_2 = [i ** 2 for i in range(1,11)]
print(square_2)
print(square_2[3:9:2])