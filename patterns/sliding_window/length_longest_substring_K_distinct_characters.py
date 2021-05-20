# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string

# Example:
# s = "araaci", k = 2
# Output: 4 
# This is because the longest substring with no more than '2' 
# distinct characters is "araa"

def longest_substring_with_k_distinct(str, k):
  letter = {} #hashmap that remembers new characters
  windowStart = 0
  maxSub = 0
  for windowEnd in range(len(str)): #go through each character in string
    if str[windowEnd] not in letter: #if character isnt in dict, add it
      letter[str[windowEnd]] = 0 #initialize it to 0
    letter[str[windowEnd]] += 1 #add 1 to the count of character

    while len(letter) > k: #when we go over the distinct amount
      letter[str[windowStart]] -= 1 #decrement letter at start
      if letter[str[windowStart]] == 0: #remove once count gets to 0
        del letter[str[windowStart]]
      windowStart += 1 #shrink window 
    
    maxSub = max(maxSub, (windowEnd - windowStart) + 1) #remember the max
  
  return maxSub

#time complexity: O(N + N) -> O(N)
#space complexity: O(K)