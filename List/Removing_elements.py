# By using del Statement
motorcycle = ['honda', ' yamaha', 'suzuki', 'ducati', 'tiger', 'Harley']
# print(motorcycle)

# del  motorcycle[1]
# print(motorcycle)

# By using pop() method
# It removes last item of list, but it let you works with it.
# popped_motorcycle = motorcycle.pop()
# print(motorcycle)

# print(popped_motorcycle)

# Another use case
# first_owned = motorcycle.pop(0)
# print(f"The first motorcycle I owned was a {first_owned} ")


# # Removing an Item by value
# motorcycle.remove('tiger')
# print(motorcycle)

# We can reuse removed value also

too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
reason = f"{too_expensive} is too expensive for me"
print(reason)