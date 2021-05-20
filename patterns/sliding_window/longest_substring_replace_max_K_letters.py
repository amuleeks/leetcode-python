# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement

# Example:
# str = "aabccbb", k = 2
# Output: 5
# Replace the 2 'c' with 'b' for longest repeating substring "bbbbb"

def length_of_longest_substring(str, k):
  frequency = {} #to count frequency of letters
  maxRepeat = 0 # counts how many times something is repeated
  maxLength = 0 # counts max length of string
  windowStart = 0
  for windowEnd in range(len(str)): #for every letter in str
    rightChar = str[windowEnd] #assign rightmost char in window
    if rightChar not in frequency: # if not in map
      frequency[rightChar] = 0 # add to map
    frequency[rightChar] += 1 #iterate the count 
    maxRepeat = max(maxRepeat, frequency[rightChar]) 
#use the one that repeats the most as the "main" string
    if (windowEnd - windowStart + 1) - maxRepeat > k:
      leftChar = str[windowStart]
      frequency[leftChar] -= 1
      windowStart += 1

    maxLength = max(maxLength, (windowEnd - windowStart) + 1)

  return maxLength

#time complexity: O(N)
#space complexity: O(1), because there are a fixed amount of letters in the english alphabet
