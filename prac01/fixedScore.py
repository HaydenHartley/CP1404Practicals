"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))

while 100 >= score >= 0:
    if score >= 50:
        print("passable")
    elif score >= 90:
        print("excellent")
    else:
        print("bad")
    score = float(input("Enter score: "))
print("invalid score")