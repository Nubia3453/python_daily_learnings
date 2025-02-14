# Check if a set is a subset or superset of another set.
# set a 
# set b 
# a is subset of b, if some of the elements of a are in b
# a is superset of b, if all elements of b are in a

a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
# it reads as b is subset of a
print(b.issubset(a)) # False

# it reads as a is superset of b
print(a.issuperset(b))
