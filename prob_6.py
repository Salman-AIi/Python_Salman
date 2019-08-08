#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

#-------SOLUTION--------#

nums = (2,6,4,4,3,7,9,2,2,4)

def count_evens(nums):
    even_list = []
    for i in nums:
        if (i % 2 == 0):
            even_list.append(i)
    print(len(even_list))
                

count_evens(nums)


  