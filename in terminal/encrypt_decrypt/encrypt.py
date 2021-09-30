import random
import string
encrypt = {"a": "u", "b": "v", "c": "w", "d": "x", "e": "y", "f": "z", "g": "1", "h": "2",
           "i": "3", "j": "4", "k": "5", "l": "6", "m": "7", "n": "8", "o": "9", "p": "m",
           "q": "a", "r": "b", "s": "c", "t": "d", "u": "e", "v": "f", "w": "g", "x": "h",
           "y": "i", "z": "j", "1": "k", "2": "l", "3": "n", "4": "o", "5": "p", "6": "q",
           "7": "r", "8": "s", "9": "t"}

decrypt = {'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd', 'y': 'e', 'z': 'f', '1': 'g', '2': 'h', '3': 'i', '4': 'j', '5': 'k', '6': 'l', '7': 'm', '8': 'n', '9': 'o', 'm': 'p', 'a': 'q', 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f':
           'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z', 'k': '1', 'l': '2', 'n': '3', 'o': '4', 'p': '5', 'q': '6', 'r': '7', 's': '8', 't': '9'}

# decrypt = {}
# keys = list(encrypt.keys())
# values = list(encrypt.values())
# for i in range(len(keys)):
#     decrypt[values[i]] = keys[i]
# print(decrypt)


def encryptText(text):
    newText = ""
    for i in text:
        newText += encrypt[i]
    return newText


def decryptText(text):
    newText = ""
    for i in text:
        newText += decrypt[i]
    return newText


def generateRandomText():
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ/*-=+_!@~#$%^&*()?><:}{"
    r = random.randint(1, 10)
    text = ''
    for i in range(r):
        x = random.randint(0, len(s)-1)
        text += s[x]
    return text


def hardEncrypt(text):
    newText = ""
    for i in text:
        newText += encrypt[i] + generateRandomText()
    return newText


def isValidInput(text):
    validInputs = string.ascii_lowercase+string.digits
    isValid = True
    for i in text:
        if i not in validInputs:
            isValid = False
    return isValid


def extractValidText(text):
    validInputs = string.ascii_lowercase+string.digits
    validText = ""
    for i in text:
        if i in validInputs:
            validText += i
    return validText
