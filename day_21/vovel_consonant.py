# vovel are charaters a, e, i, o, u:
# consonants are all other characters.
import random
# Create a list of vovel:
vovels=['a','e','i','o','u']
char=random.choice('abcdefghijklmnopqrstuvwxyz')
if char in vovels:
    print(f"{char} is a vovel")
else:
    print(f"{char} is a consonant") 