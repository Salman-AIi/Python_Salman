import random
random_num = random.randint(100,200)

print(random_num)

print('Welcome To The Guessing Game!')
inputno = int(input('Enter A Number Between 100-299:-'))

while inputno != random_num:
    if inputno > 100 and inputno < 200:
        print('Welcome To The Guessing Game!')
        inputno = int(input('Enter A Number Between 100-299:-'))
    if inputno <= 100 and inputno >= 200:
        print('Please Enter A Number Between 100-200!')
        homie =  input('Do You Want Guess Again?')
        if homie == 'Y' or 'y':
            while inputno != random_num:
    if inputno > 100 and inputno < 200:
        inputno = int(input('Enter A Number Between 100-299:-'))
    if inputno == random_num:
        print('OMG thats right!')
        break
    random.shu