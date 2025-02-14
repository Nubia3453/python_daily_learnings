# **********************************************
# Find the position of a substring in a string.
# **********************************************

test_string='Find the position of a substring in a string'.lower()
test_substring='sub'
if 'string' in test_string:
    output=test_string.index(test_substring)
    
else:
    print('Substring not found') 
print('************************************************************************************')
print('This program check substring is part of given string and returns its index.')
print('************************************************************************************')
print('Main string:', test_string)
print('Substring: ',test_substring)
print("substring '{}' is at {} position.".format(test_substring,output))
print('************************************************************************************')