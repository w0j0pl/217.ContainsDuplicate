class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}

        for ch in s1:
            dict_s1[ch] = 1 + dict_s1.get(ch, 0)

        dict_s2 = {}
        left = 0

        for i, ch in enumerate(s2):
            dict_s2[ch] = 1 + dict_s2.get(ch, 0)

            if i - left == len(s1) - 1:
                if dict_s1 == dict_s2:
                    return True
                
                else:        
                    dict_s2[s2[left]] -= 1
                    
                    if dict_s2[s2[left]] == 0:
                        dict_s2.pop(s2[left])

                    left += 1

        return False