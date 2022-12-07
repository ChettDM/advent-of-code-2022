import os

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()

def all_characters_are_different(set: str):
    for i in range(4):
        for j in range(4):
            if i == j:
                continue

            if set[i] == set[j]:
                return False
    return True


# print(lines[0][0:4])

for i in range(0, len(lines[0]), 1):
    word = lines[0][i:i+4]
    # print(word)

    if all_characters_are_different(word):
        print(word)
        print(i+4)
        break
