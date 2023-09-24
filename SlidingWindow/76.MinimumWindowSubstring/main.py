class Solution:
    def minWindow(self, s: str, t: str) -> str:     
        t_dict = Counter()
        for ch in t: t_dict[ch] += 1
            
        remaining = len(t)
        ans = math.inf
        idx = -1
        left = 0

        for right, ch in enumerate(s):
            if t_dict[ch] > 0: 
                remaining -= 1
            t_dict[ch] -= 1

            while remaining == 0:
                if right - left + 1 < ans:
                    ans = right - left + 1
                    idx = left

                if t_dict[s[left]] == 0: 
                    remaining += 1

                t_dict[s[left]] += 1
                left += 1
        
        return "" if idx == -1 else s[idx:idx+ans]