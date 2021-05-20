# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example:
# arr = [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0 1]]

def search_triplets(arr):
  triplets = []
  arr.sort()
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets

def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while left < right:
    current_sum = arr[right] + arr[left]
    if current_sum == target_sum :
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1
      while left < right and arr[right] ==arr[right + 1]:
        right -= 1
    elif target_sum > current_sum:
      left += 1
    else:
      right -= 1

# time complexity: sorting array takes O(N * log(N)), searchPair() takes O(N), we call searchPair() for every number in the input array so the overall
# search_triplets() will take O(N * log(N) + N^2) which is equivalent to O(N^2)

#space complexity: O(N)
