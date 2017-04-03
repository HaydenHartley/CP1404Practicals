"""
CP1404/CP5632 Practical
colour hexadecimal codes in a dictionary
"""
COLOUR_HEX_CODE = {"AliceBlue": "#f0f8ff", "BlanchedAlmond": "#ffebcd", "DarkGoldenrod": "#b8860b",
            "DarkOrchid": "#9932cc", "red1": "#ff0000", "green1": "00ff00", "blue1": "0000ff"}

colour = input("enter a colour name:")
while colour != "":
    if colour in COLOUR_HEX_CODE:
        print(colour, "has hexadecimal code", COLOUR_HEX_CODE[colour])
    else:
        print("invalid name")
    colour = input("enter a colour name:")
