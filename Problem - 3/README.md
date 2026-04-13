# 🚀 Longest Substring Without Repeating Characters

<p align="center">
  <img src="https://img.shields.io/badge/LeetCode-Problem%203-orange?style=for-the-badge&logo=leetcode" />
  <img src="https://img.shields.io/badge/Language-Java-blue?style=for-the-badge&logo=java" />
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen?style=for-the-badge" />
</p>

---

## 📌 Problem Overview

> Given a string `s`, find the length of the **longest substring without repeating characters**.

---

## 🧾 Example

```text
Input:  "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring
```

---

## 🎬 Visual Animation (Sliding Window)

```text
String:  a   b   c   a   b   c   b   b
Index:   0   1   2   3   4   5   6   7

Step 1: [a b c] → valid ✅ length = 3
Step 2: duplicate 'a' → shift window →
        [b c a]
Step 3: continue sliding →
        [c a b]
Step 4: duplicate 'b' → shift again
```

👉 Window expands ➡️
👉 On duplicate → shrink from left ⬅️

---

## 🧠 Core Idea (Diagram)

```text
           right →
        ┌──────────────┐
        │  sliding     │
left →  │   window     │
        └──────────────┘

Rule:
- Expand → if no duplicate
- Shrink → if duplicate found
```

---

## ⚙️ Approach

### 🔹 Java

* Use `HashMap` → stores last index of each character
* Move `left` pointer smartly using `Math.max()`

### 🔹 Python

* Use `Set` → track current window characters
* Remove duplicates using `while` loop

---

## ⚡ Complexity

| Type     | Value |
| -------- | ----- |
| 🕒 Time  | O(n)  |
| 💾 Space | O(n)  |

---

## ☕ Java Implementation

```java
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int left = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);

            if (map.containsKey(ch)) {
                left = Math.max(left, map.get(ch) + 1);
            }

            map.put(ch, right);
            result = Math.max(result, right - left + 1);
        }

        return result;
    }
}
```

---

## 🐍 Python Implementation

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
       
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

## 🔥 Key Insights

* Use **Sliding Window** to avoid nested loops
* Use **HashMap / Set** for fast lookup
* Always ensure:

  ```text
  left pointer NEVER moves backward
  ```

---

## 🎯 Why This Problem is Important

✅ Frequently asked in interviews
✅ Builds strong DSA fundamentals
✅ Teaches optimization (O(n²) → O(n))

---

## 🌟 Bonus Tip

If you understand this problem well, you can solve:

* Longest substring with K distinct characters
* Minimum window substring
* Sliding window maximum

---

## ⭐ Show Some Love

If you found this useful:

```text
⭐ Star this repo
🍴 Fork it
📢 Share it
```

---

<p align="center">
  Made with ❤️ by Developer
</p>
