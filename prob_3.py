#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

words = ('Hiabc' , 'abc')
def arrayCheck(words):
   for i in range(len(words)-2):
       if words[0][:4]==a and words[i+1]==2 and words[i+2]==3 :
           return True
   return False
print(arrayCheck(words))
    