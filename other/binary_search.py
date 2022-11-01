# only works on sorted lists 
# checks if target number if exists in list and returns true, false otherwise
from operator import truediv


def binary_search(sorted_list, target):
    smallest, largest = 0, len(sorted_list) - 1
    mid = (largest + smallest) // 2

    while (smallest <= largest):
        current_num = sorted_list[mid]
        if (current_num < target) :
            smallest = mid + 1
        elif (current_num > target):
            largest = mid - 1
        elif current_num == target:
            return True

        mid = (largest + smallest) // 2
        
    
    return False

def generate_sorted_list(length_of_list):
    res = []
    for i in range(1, length_of_list + 1):
        res.append(i)
    print(res)
    return res



print(binary_search(generate_sorted_list(100), 1))