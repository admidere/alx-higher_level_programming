#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sep = (".", "?", ":")
    new_text = ""
    for letter in text:
        new_text += letter
        if letter in sep:
            new_text += "\n"
            print(new_text.strip(" "))
            new_text = ""
    if letter not in sep:
        print(new_text.strip(" "), end="")
