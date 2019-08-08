###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

# Another hint:

#list_guess = []
guess = list(input("What is your guess? "))


for i in range(0, len(guess)): 
    guess[i] = int(guess[i])
#noob = (guess.split())
#print(noob)
#list_guess.append(noob)
print(guess)

close = False
correct = False
wrong = False


def correct(correct):
    if digits == guess:       
        zee = True
        correct = True
        if zee == True:
            print('THATS RIGHT!')
def close(close):
    if digits[0] or digits[1] or digits[2] == guess[0] or guess[1] or guess[3]:
        
        homie = True
        close = True
        wrong = False
        if homie == True:
            print('You Are Close!')
                        
def wrong(wrong):
    if digits != guess:       
        yo = True
        if close == False:
            wrong = True
        if yo == True:
            print('Get The Hell Outta Here Thats Wrong ;-;')


close(close)
if close == True:
    correct = True
    wrong = False
correct(correct)
if correct == True:
    close = False
    wrong = False
wrong(wrong)
if wrong == True:
    close = False
    correct = False


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
