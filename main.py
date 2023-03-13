# ESTABLISH ALPHABETS

eng_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "?", ":", "'", "-",
             "/", "(", ")", '"', " "]

morse_alpha = [".- ", "-... ", "-.-. ", "-.. ", ". ", "..-. ", "--. ", ".... ", "..  ", ".--- ", "-.- ", ".-.. ", "-- ",
               "-. ", "--- ", ".--. ", "--.- ", ".-. ", "... ", "- ", "..- ", "...- ", ".-- ", "-..- ", "-.-- ", "--.. ",
               "----- ", ".---- ", "..--- ", "...-- ", "....- ", "..... ", "-.... ", "--... ", "---.. ", "----. ",
               ".-.-.- ", "--..-- ", "..--.. ", "---... ", ".----. ", "-....- ", "-..-. ", "-.--.- ", "-.--.- ",
               ".-..-. ", "   "]

# SET START STATE

translating = True

# CREATE FUNCTIONS


def get_text():
    """Gets text to convert as input from user"""
    text_to_convert = input("Please enter the text you would like to convert:\n")
    return text_to_convert


def translate_again():
    """Asks if user wants to make another translation"""
    do_again = input("Would you like to make another translation? (Y/N) ").lower()
    if do_again == "n":
        print("Thanks for using Katie's Magical Morse Code Converter!")
        return False
    elif do_again == "y":
        return True
    else:
        print("I'm sorry, that is not a valid response.")
        response = translate_again()
        return response


# RUN THE PROGRAM

while translating:

    # GREET AND ASK FOR INPUT

    print("Welcome to Katie's Magical Morse Code Converter! You enter text and we'll convert it to Morse Code.")
    text = get_text().lower()

    # SPLIT TEXT INTO CHARACTERS

    character_list = list(text)

    # CREATE LIST TO HOLD TRANSLATED CHARACTERS

    translation = []

    # LOOP THROUGH CHARACTERS

    for c in character_list:

        # CHECK FOR INVALID CHARACTERS

        if c not in eng_alpha:
            print("I'm sorry, you've entered an invalid character! Please try again.")
            translation = []
            break

        # TRANSLATE CHARACTERS

        else:
            i = eng_alpha.index(c)
            morse_char = morse_alpha[i]
            translation.append(morse_char)

    # JOIN CHARACTERS IF ALL VALID

    if translation != []:

        morse_text = "".join(translation)

        # PROVIDE TRANSLATION

        print(f"Here is your translation:\n\n{morse_text}")

        # BACK TO START OR END PROGRAM

        translating = translate_again()
