# More readable program
values = []
for value in list(range(1,11)):
    cube = value ** 3
    values.append(cube)
print(values)



## list comprehension
cubes = [number ** 3 for number in range(1,11)]
print(cubes)