guests = ['Ben', 'Stok', 'Alh4zr3d', 'John', 'Live', 'Alex']
# message = f"Dear {guests[2]}, I'm inviting you at my home for dinner on this sunday. I hope you'll come at my place."
# print(message)

# Not_coming = guests.pop(2)
# print(f"Guys, {Not_coming} couldn't make it. He's busy on sunday also !!")
guests[2] = 'Jasson'
# # message = f"Dear {guests[2]}, I'm inviting you at my home for dinner on this sunday. I hope you'll come at my place."
# # print(message)
# # print(guests)

# print(f"Hey {guests[1]}, I've found bigger table")
guests.insert(0, 'Hac')
guests.insert(3, 'earth')
guests.append('Farah')
# print(f"Dear {guests[0]}, {guests[3]} and {guests[-1]}, I'm inviting you at my home for dinner on this sunday. I hope you'll come at my place.")
print(len(guests))
print(guests)
print(f"Hey {guests[0]}, I can invite two people only")
popped_guest = guests.pop(0)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

print(f"Hey {guests[1]}, I can invite two people only")
popped_guest = guests.pop(1)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

print(f"Hey {guests[2]}, I can invite two people only")
popped_guest = guests.pop(2)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

print(f"Hey {guests[3]}, I can invite two people only")
popped_guest = guests.pop(3)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

print(f"Hey {guests[-2]}, I can invite two people only")
popped_guest = guests.pop(-2)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

print(f"Hey {guests[-1]}, I can invite two people only")
popped_guest = guests.pop(-1)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

print(f"Hey {guests[1]}, I can invite two people only")
popped_guest = guests.pop(1)
print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")

# print(f"Hey {guests[5]}, I can invite two people only")
# popped_guest = guests.pop(5)
# print(f"I'm sorry to inform you {popped_guest}, that I cannot invite you")
print(len(guests))
print(guests)

print(f"{guests[0]} you're still invited to dinner")
print(f"{guests[1]} you're still invited to dinner")
print(len(guests))
del guests[0]
del guests[0]

print(guests)

print(len(guests))