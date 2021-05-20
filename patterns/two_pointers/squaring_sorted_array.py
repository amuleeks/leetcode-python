# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Example: 
# arr = [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

def make_squares(arr):
  length = len(arr)
  squares = [0 for x in range(length)] 
  highestSquareIdx = length - 1
  left, right = 0, length - 1
  while left <= right:
    leftsq = arr[left] * arr[left]
    rightsq = arr[right] * arr[right]
    if leftsq > rightsq:
      squares[highestSquareIdx] = leftsq
      left += 1
    else:
      squares[highestSquareIdx] = rightsq
      right -= 1
    highestSquareIdx -= 1

  return squares

# time complexity: O(N)
# space complexity: O(N)