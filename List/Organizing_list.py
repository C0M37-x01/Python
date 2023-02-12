# sort() method
# We've sorted this list permanently we can't revert back this process
cars = ['Rolls Royse', 'Ferrari', 'BMW', 'Audi', 'Nissan']
# cars.sort()
# print(cars)

# # We want to sort in reverse order 

# cars.sort(reverse=True)
# print(cars)

# # Sorting a List Temporarily with sorted() function
# print("Here is the original list: ")
# print(cars)

# print("\nHere is the sorted list: ")
# print(sorted(cars))

# print("\nHere is the sorted list but in reverse order: ")
# print(sorted(cars, reverse=True))

# print("\nHere is the Original list again: ")
# print(cars)


# Printing List in Reverse Order by using reverse() method
# It also change order of list permanently but we ca nrevrt it back by using reverse() method again
print(cars)

cars.reverse()
print(cars)

# Finding the Length of a list

print(len(cars))