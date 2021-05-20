#Given an array, find the average of all continuous subarrays of size 'K' in it

#the brute force approach is the following

def avg_of_subarrays(K, arr):
    result = [] #place to store all of the averages
    for i in range(len(arr)-K+1):
        sum = 0.0
        for j in range(i, i+K):
            sum += arr[j]
        result.append(sum/K)
    return result

#time complexity: O(N*K)
#space complexity: O(1)

#efficient algorithm is shown below 

def avg_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K - 1:
            result.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result

#time complexity: O(N)
#space complexity: O(1)