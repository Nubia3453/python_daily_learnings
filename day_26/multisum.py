# Create a function that accepts multiple arguments and returns their sum.

def accept_numbers():
    numbers = []
    import random
    for i in range(1,5):
        num=random.randint(1,50)
        numbers.append(num)
    return numbers
def num_sum(numbers):
    print(sum(numbers)) 

def main():
    numbers = accept_numbers()
    result=num_sum(numbers)
    return result

main()
# 

