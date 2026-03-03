# Add Two Numbers – LeetCode Problem 2

## 🔗 Problem Link

https://leetcode.com/problems/add-two-numbers/

---

## 📘 Problem Statement

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

### Example

Input:

```
l1 = [2,4,3]
l2 = [5,6,4]
```

Output:

```
[7,0,8]
```

Explanation:

```
342 + 465 = 807
```

Since digits are stored in reverse order:

```
2 -> 4 -> 3
5 -> 6 -> 4
```

Result:

```
7 -> 0 -> 8
```

---

# 💡 Approach

We simulate elementary school addition digit by digit.

### Key Idea:

* Traverse both linked lists simultaneously.
* Add corresponding digits along with any carry from the previous step.
* Store the result digit in a new linked list.
* Continue until both lists and carry are fully processed.

We use:

* A **dummy node** to simplify linked list construction.
* A **carry variable** to handle sums ≥ 10.

---

# 🧠 Algorithm Steps

1. Create a dummy node.
2. Initialize `carry = 0`.
3. Traverse while:

   * `l1` exists OR
   * `l2` exists OR
   * `carry` is non-zero.
4. Compute:

   ```
   total = val1 + val2 + carry
   carry = total // 10
   digit = total % 10
   ```
5. Append new node with `digit`.
6. Move to next nodes.
7. Return `dummy.next`.

---

# ⏱ Time Complexity

```
O(max(n, m))
```

Where:

* `n` = length of first list
* `m` = length of second list

We traverse both lists once.

---

# 📦 Space Complexity

```
O(max(n, m))
```

A new linked list is created to store the result.

---

# 🐍 Python Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

---

# ▶️ Running the Program (Local Version)

Example execution:

```
Result:
7 -> 0 -> 8
```

---

# 📁 Project Structure

```
Leetcode/
│
├── Problem - 1
│
├── Problem - 2
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

# 🚀 Concepts Used

* Linked List
* Carry Handling
* Dummy Node Technique
* Simulation of Arithmetic

---

# 👨‍💻 Author

Niraj Singh
