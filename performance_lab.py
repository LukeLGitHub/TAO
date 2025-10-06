# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    
    most_common = max(freq, key=freq.get)
    return most_common

# Test Cases
print(most_frequent([1,3,2,3,4,1,3]))
print(most_frequent([1,1,2,2]))
print(most_frequent([5]))
print(most_frequent([]))
print(most_frequent([7,7,7,7,7]))

"""
Time and Space Analysis for problem 1:
- Best-case: O(n), It still has to look at every number once to count how many times each appears.
- Worst-case: O(n), Even is every number is different, we still loop through all of them and then find the one with the highest count.
- Average-case: O(n), On average, we'll still go through all the numbers once.
- Space complexity: O(k), Where k is how many unique numbers there are. If all numbers are different, thats basically O(n)
- Why this approach? Using a dictionary makes it fast to count how many times each number shows up. Its simple and works well for most cases.
- Could it be optimized? You could use Python's built in counter class to make the code shorter, but it wouldnt actually be faster.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

# Test Cases
print(remove_duplicates([4,5,4,6,5,7]))
print(remove_duplicates([1,1,1,1]))
print(remove_duplicates([]))
print(remove_duplicates([10,20,30]))
print(remove_duplicates([3,3,2,1,2,3]))
"""
Time and Space Analysis for problem 2:
- Best-case: O(n), We have to check every element once, even if there are no duplicates.
- Worst-case: O(n), still need to loop through all elements and check/set membership each time.
- Average-case: O(n), checking and adding to a set is O(1) on average, so overall it stays linear.
- Space complexity: O(n), in the worst case (all elements unique), we store every number once in both the list and set.
- Why this approach? Using a set makes it faster to check if we've seen a number, and keeping a list lets us preserve the order they appeared in.
- Could it be optimized? I dont think so, this is already an efficent approach. You could use a dictionary or an OrderedDict, but it would work about the same.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.append((complement, n))
        seen.add(n)
    return pairs

# Test Cases
print(find_pairs([1,2,3,4], 5))
print(find_pairs([2,4,6,8,10], 12))
print(find_pairs([1,3,5,7], 10))
print(find_pairs([1,2,3], 10))
print(find_pairs([], 5))
"""
Time and Space Analysis for problem 3:
- Best-case: O(n), even if no pairs are found, we still have to look through each number once.
- Worst-case: O(n), We still only loop through the list once, checking for complements in a set
- Average-case: O(n), set lookups and insertions are O(1) on average, so the total stays linear.
- Space complexity: O(n), we store seen numbers and pairs, which could take up to n elements combined.
- Why this approach? Using a set makes it quick to check if weve already seen the needed complement for a pair. 
- Could it be optimized? I dont think so, this is already optimal for an unsorted list. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    arr = [None] * capacity

    for i in range(n):
        if size == capacity:
            print(f"Increasing capacity from {capacity} to {capacity * 2}")
            new_arr = [None] * (capacity * 2)
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity *= 2

        arr[size] = i
        size += 1

    print("Final array:", arr[:size])

# Test Cases
add_n_items(6)
add_n_items(1)
add_n_items(10)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Every time the number of items reaches the current capacity (1, 2, 4, 8, 16, ...)
- What is the worst-case for a single append? O(n), when a resize happens, because we copy all current elements into a new list
- What is the amortized time per append overall? O(1), on average. Even though some operations are expensive, most are cheap. Over many appends, the total time divided by n stays constant.
- Space complexity: O(n), we only keep one list that grows as needed to hold all elements.
- Why does doubling reduce the cost overall? Because doubling makes resizing less frequent. Each time the list grows it can handle twice as many appends before resizing again.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    current_sum = 0
    for n in nums:
        current_sum += n
        totals.append(current_sum)
    return totals

# Test Cases
print(running_total([1, 2, 3, 4]))
print(running_total([5, 5, 5]))
print(running_total([10]))
print(running_total([]))
print(running_total([1, -1, 2, -2]))
"""
Time and Space Analysis for problem 5:
- Best-case: O(n), we need to go through every number to compute the running sum.
- Worst-case:O(n), same as best case, each element is processed once
- Average-case: O(n), every element is summed once, so linear time overall
- Space complexity: O(n), we create a new list to store the running totals
- Why this approach? It is simple and efficient, just keep a running sum and append to a new list.
- Could it be optimized? I dont think so, its already O(n). You could do it in place to save some memory if modifying the original list is okay, but that changes the input.
"""

# ---Optimized---
# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates_optimized(nums):
    return list(dict.fromkeys(nums))

# Test Cases
print(remove_duplicates([4,5,4,6,5,7]))
print(remove_duplicates([1,1,1,1]))
print(remove_duplicates([]))
print(remove_duplicates([10,20,30]))
print(remove_duplicates([3,3,2,1,2,3]))