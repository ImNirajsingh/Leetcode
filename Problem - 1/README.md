# Two Sum – LeetCode Problem 1

## Problem Link

https://leetcode.com/problems/two-sum/

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

Return the answer in any order.

### Example

Input:

```
nums = [2,7,11,15]
target = 9
```

Output:

```
[0,1]
```

Because:

```
nums[0] + nums[1] = 2 + 7 = 9
```

---

# Approach

This solution uses a **Hash Map (Dictionary)**.

Idea:

1. Iterate through the array.
2. For each number, compute the **complement** needed to reach the target.
3. Check if the complement already exists in the dictionary.
4. If yes, return the stored index and current index.
5. Otherwise store the current number with its index.

This allows us to find the solution in **one pass**.

---

# Algorithm

1. Create an empty dictionary `seen`.
2. Loop through array using `enumerate`.
3. Compute `complement = target - num`.
4. If complement exists in dictionary → return indices.
5. Otherwise store current number and index.
6. Continue until solution is found.

---

# Time Complexity

```
O(n)
```

We traverse the list once.

---

# Space Complexity

```
O(n)
```

Dictionary stores up to `n` elements.

---

# Python Implementation

```python
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return seen[complement], i
        
        seen[num] = i
    
    return None
```

---

# Running the Program

Example run:

```
Enter number of elements: 4
Enter elements separated by space: 2 7 11 15
Enter target: 9
```

Output:

```
Indices: 0 1
```

---

# Author

Niraj Singh
