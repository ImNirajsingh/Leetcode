# 🚀 Median of Two Sorted Arrays

<p align="center">
  <img src="https://img.shields.io/badge/LeetCode-Problem%204-orange?style=for-the-badge&logo=leetcode"/>
  <img src="https://img.shields.io/badge/Language-Java-blue?style=for-the-badge&logo=java"/>
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Approach-Merge%20%2B%20Sort-green?style=for-the-badge"/>
</p>

---

## 📌 Problem Overview

> Given two sorted arrays `nums1` and `nums2`, return the **median** of the two sorted arrays.

---

## 🎬 Animation (How It Works)

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="500"/>
</p>

### 🔍 Step-by-step Flow

```text
nums1 = [1, 3]
nums2 = [2]

➡️ Merge:
[1, 2, 3]

➡️ Find middle:
Median = 2 ✅
```

---

## 🎥 Visual Sliding Animation

```text
Step 1:
[1, 3] + [2]
        ↓

Step 2:
[1, 2, 3]
        ↓

Step 3:
   ↑
  Median = 2
```

---

## 🧠 Even Length Animation

```text
nums1 = [1, 2]
nums2 = [3, 4]

Merged:
[1, 2, 3, 4]

Middle Elements:
     ↑   ↑
     2   3

Median = (2 + 3) / 2 = 2.5
```

---

## ⚙️ Approach

### 🔹 Steps:

1. Merge both arrays
2. Sort the merged array
3. Find median:

   * Odd → middle element
   * Even → average of two middle elements

---

## ⚡ Complexity

| Type     | Value             |
| -------- | ----------------- |
| 🕒 Time  | O((m+n) log(m+n)) |
| 💾 Space | O(m+n)            |

---

## 🐍 Python 3 Implementation

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)

        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
```

---

## ☕ Java Implementation

```java
import java.util.Arrays;

public class problem4 {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] mergedArray = new int[nums1.length + nums2.length];

        System.arraycopy(nums1, 0, mergedArray, 0, nums1.length);
        System.arraycopy(nums2, 0, mergedArray, nums1.length, nums2.length);

        Arrays.sort(mergedArray);

        int n = mergedArray.length;

        if (n % 2 == 0) {
            return (mergedArray[n / 2 - 1] + mergedArray[n / 2]) / 2.0;
        } else {
            return mergedArray[n / 2];
        }
    }
}
```

---

## 🔥 Key Insights

* Simple & beginner-friendly approach
* Uses built-in sorting
* Easy to visualize and debug

---

## ⚠️ Interview Note

👉 This is a **brute-force approach**

* Optimal solution: **O(log(min(m,n)))**
* Uses binary search (advanced level)

---

## 🌟 Bonus Practice

* Kth smallest element in sorted arrays
* Median in data stream
* Binary search partition method

---

## ⭐ Support

```text
⭐ Star this repo
🍴 Fork it
🚀 Keep coding!
```

---

<p align="center">
  Made with ❤️ by Developer
</p>
