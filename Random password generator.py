#Random password generator
import string
import random

def generate_password(min_length,numbers=True,special_characters=True):
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation

    characters=s1
    if numbers:
        characters+=s2
    if special_characters:
        characters+=s3
    
    pwd=""
    meets_criteria=False
    has_numbers=False
    has_special=False

    while not meets_criteria or len(pwd) < min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in s2:
            has_numbers=True
        elif new_char in s3:
            has_special=True
        
        meets_criteria=True
        if numbers:
            meets_criteria=has_numbers
        if special_characters:
            meets_criteria+=has_special
    return pwd

min_length=int(input("Enter Password length:"))
has_numbers=input("Do You Want Numbers (y/n)?").lower()=="y"
has_special=input("Do You Want TO Have Special Character (y/n)?").lower()=="y"
pwd=generate_password(min_length,has_numbers,has_special)
print("Your Password is:",pwd)