class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # for i in range(0, len(numbers)):
        #     while numbers[i] < numbers[i+1]:
        #         if numbers[i] + numbers[i+1] == target:
        #             return [numbers[i], numbers[i+1]]
        #         i +=1
        

        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1

            else:
                return [l+1, r+1]
        return []


        