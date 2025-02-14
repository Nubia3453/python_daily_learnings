from faker import Faker
fake=Faker()
sentence=fake.sentence()
word=fake.word('adverb')

# sentence = 'Write a program to count the frequency of words in a sentence'
counter={}
for i in sentence.split(' '):
    counter[i]=+1
    if word in counter:
        print(i , 'word found in sentece')
print(word)
print(sentence)
print(counter)