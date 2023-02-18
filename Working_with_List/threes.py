# Adding last argument or skipping 2 values
threes = [value for value in range(3,31,3)]
print(threes)

# Multiplying every number in range of 3 to 31
threes = []
for number in range(3,31):
    threes.append(number * 3)
print(threes)

# multiplying every number in range of 1 to 11
threes = []
for number in range(1,11):
    threes.append(number * 3)
print(threes)

## List comprehansion
threes = [number * 3 for number in range(1,11)]
print(threes)