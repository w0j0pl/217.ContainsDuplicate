class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lista = [1] * len(nums)
    
        pre = 1
        for i in range(len(nums)):
            lista[i] = pre
            pre *= nums[i]

        post = 1    
        for i in range(len(nums)-1,-1,-1):
            lista[i] *= post
            post *= nums[i]

        return lista