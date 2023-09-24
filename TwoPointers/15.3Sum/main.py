class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zbior = set()

        if nums.count(0) > 2:
            zbior.add(tuple([0, 0, 0]))

        nums = sorted(k for k, count in collections.Counter(nums).items() for _ in range(min(count, 2)))
        
        for i in range(len(nums) - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            if nums[i] >= 0:
                break
                
            start = i + 1
            end = len(nums) - 1
            while start != end:
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1

                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1

                else:
                    zbior.add(tuple([nums[i], nums[start], nums[end]]))
                    if end - start < 2:
                        break

                    else:
                        start += 1
                        end -= 1
                        
        return zbior