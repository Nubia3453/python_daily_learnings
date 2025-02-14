import re
import random

test_inputs=['The five boxing wizards jump quickly',
             'How about you PR Daily readers?',
             'The quick onyx goblin jumps over the lazy dwarf',
             'This article is a re-run as part of our countdown',
             'Puzzled women bequeath jerks very exotic gifts',
             'Try creating pangrams of your own to test your skills',
             'A pangram is a sentence or expression that uses all the letters of the alphabet.',
             'My girl wove six dozen plaid jackets before she quit'
             ]

letters='abcdefghijklmnopqrstuvwxyz'
user_input=random.choice(test_inputs)
formatted_string=user_input.lower().replace(' ','')
counter=0
checker=''
for letter in letters:
    checker=re.search(rf'{letter}',formatted_string)
    if checker is not None:
        counter+=1

if counter == 26:  # All 26 letters matched
    message = "All letters are matched. This is a pangram."
else:
    message = "Not all letters are matched. This is not a pangram."


print('*'*17,'Here is results','*'*17)
print('Given string: {}'.format(user_input)) 
print('No of letters matched: {}'.format(counter)) 
print('Result: {}'.format(message))   
print('*'*51)