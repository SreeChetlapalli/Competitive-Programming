class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            # Add the new character to the window
            count[s[right]] = count.get(s[right], 0) + 1

            # Keep track of the most frequent character
            max_freq = max(max_freq, count[s[right]])

            # If we need too many replacements, shrink window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Current window is valid
            answer = max(answer, right - left + 1)

        return answer
