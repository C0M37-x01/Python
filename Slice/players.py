players = ['mahi', 'alice', 'virat', 'yuvi', 'rohit', 'sachin']
# # slicing first 4 values from list
# print(players[0:4])
# # slicing 1st index value to 5th from list
# print(players[1:5])
# # slicing first 5 values from list
# print(players[:5])
# # slicing list from 2nd value from list
# print(players[1:])
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(f"\t{player.title()}")