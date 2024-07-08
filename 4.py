# a
passwd={'rahul':'genius','kumar':'smart','ankita':'intelligent'}
print("All the items in passwd are \n",passwd.items())
print("All the keys in passwd are \n",passwd.keys())
print("All the values in passwd are \n",passwd.values())
print("Password of rahul is ",passwd['rahul'])
passwd['ankita']='brilliant'
print("after changung the password of ankita from intelligent to brilliant")
print(passwd)

# b
import re

def count_characters(text):
    # Define regular expressions for vowels, consonants, and digits
    vowels_pattern = r'[AEIOUaeiou]'
    consonants_pattern = r'[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]'
    digits_pattern = r'[0-9]'

    # Find all matches using the patterns
    vowels = re.findall(vowels_pattern, text)
    consonants = re.findall(consonants_pattern, text)
    digits = re.findall(digits_pattern, text)

    # Count the number of matches
    vowels_count = len(vowels)
    consonants_count = len(consonants)
    digits_count = len(digits)

    return vowels_count, consonants_count, digits_count

# Example usage
text = "Hello World! 123"
vowels_count, consonants_count, digits_count = count_characters(text)
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")
print(f"Digits: {digits_count}")
