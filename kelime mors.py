import winsound
import time

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

def beep_morse(text):
    text = text.upper()

    for harf in text:

        kod = MORSE[harf]

        for sembol in kod:
            if sembol == ".":
                winsound.Beep(800, 200)   # nokta
            elif sembol == "-":
                winsound.Beep(800, 600)   # tire
            time.sleep(0.2)               # semboller arası

while True:
    kelime = input("Kelime gir  ")
    beep_morse(kelime)
