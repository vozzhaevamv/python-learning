x = ["Ryan", "Kieran", "Mark",]
def friend(x):
    friend = []
    for name in x:
        if len(name) == 4:
            friend.append(name)
    return friend 
print(friend(x))