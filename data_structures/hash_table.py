import string

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase

def letter_to_code(letter):
    if letter in lower_case_letters:
        return int(lower_case_letters.index(letter) + 97)
    if letter in upper_case_letters:
        return int(upper_case_letters.index(letter) + 65)
