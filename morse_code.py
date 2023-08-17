MORSE_CODE = (
        ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
        ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
        ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
        ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
        ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
        ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
        (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
        ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
    )
MORSE_CODE = dict(MORSE_CODE)

def encode(message):
    for char in message:
        for key, value in MORSE_CODE.items():
            if char == value:
                encoded = key + " "
                print(encoded , end ="")
def decode(message):
    print("Decoding")

def print_intro():
   print("Welcome to Texasmorse\nThis program encodes and decodes Morse code.")
def get_input():
    flag = 1
    while(flag):
        x=input("Would you like to encode (e) or decode (d):")
        if x.lower() == "e":
           character = input("What would you like to encode")
           character = character.upper()
           encode(character)
           a=input("\nwhould you like to encode another one , yes(y) or no(n)")
           if a.lower=="y":
               get_input()
           elif a.lower=="n":
               flag=0
           else:
               print("invalid")
               get_input()


        elif x.lower() == "d":
            y = input("What would you like to encode")
            decode(y)
        else:
             print("Wrong Input")







print_intro()
get_input()