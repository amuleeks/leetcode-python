# Given an array of sorted numbers, remove all duplicates from it.
#  You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Example:
# arr = [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# The first four elements after removing the duplicates
# will be [2, 3, 6, 9]

def remove_duplicates(arr):
  next_non_duplicate = 1
  i = 1
  while i < len(arr):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1
  
  return next_non_duplicate

# time complexity: O(N)
# space complexity: O(1)
