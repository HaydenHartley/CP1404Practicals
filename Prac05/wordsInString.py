"""
CP1404/CP5632 Practical
counts how many of each word are in a string input
"""
word_collection = {}

string = input("input text: ")
for word in string.split(" "):
    if word not in word_collection:
        word_collection[word] = 1
    else:
        word_collection[word] += 1

for key in word_collection:
    print("{:{}} : {}".format(key, max((len(word) for word in word_collection)), word_collection[key]))
