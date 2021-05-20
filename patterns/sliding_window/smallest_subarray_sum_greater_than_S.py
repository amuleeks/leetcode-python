# Given an array of positive numbers and a positive number ‘S,’ 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0 if no such subarray exists.

# Example:
# [2, 1, 5, 2, 3, 2], S = 7
# The smallest subarray with sum greater than or equal to '7' is [5, 2]

import math

def smallest_continuous_subarray(s, arr):
	arrSum, windowStart = 0, 0
	small = math.inf
	for windowEnd in range(len(arr)):
		arrSum += arr[windowEnd]
		while arrSum >= s:
			small = min(small, (windowEnd - windowStart) + 1)
			arrSum -= arr[windowStart]
			windowStart += 1
	if small == math.inf:
		return 0
	return small

#time complexity: O(N + N)
#space complexity: O(1)