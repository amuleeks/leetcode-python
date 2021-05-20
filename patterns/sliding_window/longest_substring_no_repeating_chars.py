# Given a string, find the length of the longest substring, which has no repeating characters.

# Example:
# str = "aabccbb" 
# Output: 3
# This is because the longest substring without any characters is "abc"

#There are 2 ways to solve this problem, below is way #1

def non_repeat_substring(str):
  # we need to store the letters somewhere to see if they have occured before
  # we also need to count the substring (which will be the length of the dict)
  # if it has occured before, we need to shrink the start of the window until it is at a
  # position where there are no duplicates
  letters = {} 
  maxLen = 0
  windowStart = 0
  for windowEnd in range(len(str)):
    if str[windowEnd] not in letters:
      letters[str[windowEnd]] = 0
    letters[str[windowEnd]] += 1
    
    while letters[str[windowEnd]] > 1:
      letters[str[windowStart]] -= 1
      if letters[str[windowStart]] == 0:
        del letters[str[windowStart]]
      windowStart += 1
    
    maxLen = max(maxLen, len(letters))
  
  return maxLen

# then theres way #2

def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window
		# from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not 
			# have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last 
			# index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

#time complexity: O(N)
#space complexity: O(K), but since there are a fixed amount of letters in the alphabet, it can be considered as O(1)
