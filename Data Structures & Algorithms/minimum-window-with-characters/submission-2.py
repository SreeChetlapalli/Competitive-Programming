class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        dict1 = {}
        dict2 = {}

        for c in t:
            if c not in dict1:
                dict1[c] = 0
                dict2[c] = 0
            dict1[c] += 1

        required = len(dict1)
        formed = 0

        x = 0
        y = 0
        answer = ""

        while y < len(s):

            if s[y] in dict1:
                dict2[s[y]] += 1

                if dict2[s[y]] == dict1[s[y]]:
                    formed += 1

            while formed == required:

                if answer == "" or y - x + 1 < len(answer):
                    answer = s[x:y + 1]

                if s[x] in dict1:
                    if dict2[s[x]] == dict1[s[x]]:
                        formed -= 1

                    dict2[s[x]] -= 1

                x += 1

            y += 1

        return answer