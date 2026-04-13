// Longest Substring Without Repeating Characters

import java.util.HashMap;
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