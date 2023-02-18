squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

## another Methods

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# List comprehensions
squares = [num**2 for num in range(1,11)]
print(squares)