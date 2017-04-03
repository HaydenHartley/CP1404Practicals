"""
CP1404/CP5632 Practical
counts how many of each word are in a string input
"""
WORD_COLLECTION = {}

string = input("input text: ")
for word in string.split(" "):
    if word not in WORD_COLLECTION:
        WORD_COLLECTION[word] = 1
    else:
        WORD_COLLECTION[word] += 1

for key in WORD_COLLECTION:
    print("{:12} : {}".format(key, WORD_COLLECTION[key]))
