#Création du dictionnaire
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 'É': '..-..', 'È': '.-..-', 'À': '.--.-',
    'Ç': '-.-..', ' ': '/', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '!': '-.-.--', "'": '.----.', ':': '---...', ';': '-.-.-.', '-': '−····−',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

#Convertion du texte en code Morse
def text_to_morse(text):
    morse_code = " "
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + " "
        else:
            morse_code += char
    return morse_code

#Convertion du code Morse en texte
def morse_to_text(morse_code):
    text = " "
    morse_code += " "
    i = 0
    char = " "
    for morse_char in morse_code:
        if (morse_char != " "):
            i = 0
            char += morse_char
        else:
            i += 1
            if i == 2:
                text += " "
            else:
                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(char)]
                char = " "
    return text


#Demande à l'utilisateur ce qu'il souhaite afficher, puis affichage
r=input("Dans quel alphabet voulez-vous traduire ? (1 ➔ en morse, 2 ➔ en language naturel) : ")
if r=="1":
    texte = input("Saisir le texte ou la lettre que vous voulez traduire : ")
    morse_code = text_to_morse(texte)
    print(f"Le code Morse de '{texte}' est : {morse_code}")
elif r=="2":
    morse_code = input("Saisir le texte ou la lettre que vous voulez traduire : ")
    text_from_morse = morse_to_text(morse_code)
    print(f"Le texte décodé de '{morse_code}' est : {text_from_morse}")
else:
    print ("Je n'ai pas compris votre réponse")
