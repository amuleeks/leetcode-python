# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Example:
# str = "oidbcaf", pattern = "abc"
# Output: true
# String contains "bca" which is a permutation of the given pattern.

def find_permutation(str, pattern):
  windowStart = 0
  matched = 0
  pFrequency = {}
  for letter in pattern:
    if letter not in pFrequency:
      pFrequency[letter] = 0
    pFrequency[letter] += 1
  
  for windowEnd in range(len(str)):
    rightChar = str[windowEnd]
    if rightChar in pFrequency:
      pFrequency[rightChar] -= 1
      if pFrequency[rightChar] == 0:
        matched += 1
    
    if matched == len(pFrequency):
      return True
    
    if (windowEnd - windowStart) >= len(pattern) - 1:
      leftChar = str[windowStart]
      windowStart += 1
      if leftChar in pFrequency:
        if pFrequency[leftChar] == 0:
          matched -= 1
        pFrequency[leftChar] += 1
      
    
  return False

#time complexity: O(N + M) where N and M are the number of characters in the input string and the pattern
#space complexity: O(M), worst case whole pattern has distinct characters