#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

noob = [3,1,1,2,1,4]

#def arrayCheck(noob):
  #  for i in range(len(noob)-2):
  #      if noob[i]==1 and noob[i+1]==2 and noob[i+2]==3:
  #          return True
 #       return False
#print(arrayCheck(noob))
nums = ( 1, 1, 2,3, 4, 1)
def arrayCheck(nums):
   for i in range(len(nums)-2):
       if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3 :
           return True
   return False
print(arrayCheck(nums))
    

