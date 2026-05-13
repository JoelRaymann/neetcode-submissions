class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Ok we need to understand our problem here. A couple of negative numbers suddenly
        # change a min into max. So, we need to track minimum and maximum as current number
        # "X" can flip a min to max just because X is negative.

        if not nums:
            raise ValueError(f"nums must be non-empty")

        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for x in nums[1:]:
            prev_max = current_max
            prev_min = current_min

            current_max = max(x, x * prev_max, x * prev_min)
            current_min = min(x, x * prev_max, x * prev_min)

            answer = max(answer, current_max)

        return answer