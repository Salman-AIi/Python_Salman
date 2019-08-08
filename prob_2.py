#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'
noob = ('Heeololeo')

def string_bits(noob):
  result = ''
  for n in range(0, len(noob)):
    if n%2 == 0:
      result += noob[n]
  return result

print(string_bits(noob))
  
