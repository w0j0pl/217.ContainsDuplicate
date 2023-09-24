class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        stop = len(numbers) - 1

        while True:
            if numbers[start] + numbers[stop] > target:
                stop -= 1

            elif numbers[start] + numbers[stop] < target:
                start += 1
                
            else:
                return start + 1, stop + 1