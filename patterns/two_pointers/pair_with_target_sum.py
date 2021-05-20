# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Example: 
# arr = [1, 2, 3, 4, 6], target = 6
# Output: [1, 3]
# The numbers at index 1 and 3 add up to 6.

# Below is the brute force approach

def targetSum(arr, t):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if (arr[i] + arr[j] == t) and i != j:
				return [i, j]

# time complexity: O(N^2)
# space complexity: O(1)

# Below is the optimal 2 pointer approach

def pair_with_targetsum(arr, target_sum):
  left = 0 
  right = len(arr) - 1
  while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]
    
    if current_sum > target_sum:
      right -= 1
    else:
      left += 1
    
# time complexity: O(N)
# space complexity: O(1)

