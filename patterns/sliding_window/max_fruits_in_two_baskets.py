# Given an array of characters where each character represents a fruit tree, you are giventwo basket, 
# and your goal is to putmaximum number of fruits in each basket. 
# The only restriction is thateach basket can have only one type of fruit

def fruits_into_baskets(fruits):
  basket = {}
  maxLen = 0
  windowStart = 0
  for windowEnd in range(len(fruits)):
    if fruits[windowEnd] not in basket:
      basket[fruits[windowEnd]] = 0
    basket[fruits[windowEnd]] += 1

    while len(basket) > 2:
      basket[fruits[windowStart]] -= 1
      if basket[fruits[windowStart]] == 0:
        del basket[fruits[windowStart]]
      windowStart += 1
    
      
    maxSum = max(maxLen, (windowEnd-windowStart) + 1)
  
  return maxSum

#time complexity: O(N)
#space complexity : O(1)