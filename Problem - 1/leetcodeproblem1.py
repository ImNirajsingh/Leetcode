def two_sum(nums, target):
    seen = {}  # dictionary to store number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return seen[complement], i
        
        seen[num] = i
    
    return None


# ---- Main Program ----

n = int(input("Enter number of elements: "))

nums = list(map(int, input("Enter elements separated by space: ").split()))

target = int(input("Enter target: "))

result = two_sum(nums, target)

if result:
    print("Indices:", result[0], result[1])
else:
    print("No solution found")