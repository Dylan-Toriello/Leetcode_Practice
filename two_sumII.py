class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Finds two numbers in a sorted array that add up to a specific target.

        Args:
            numbers: A 1-indexed sorted list of integers.
            target: The target sum.

        Returns:
            A 1-indexed list containing the indices of the two numbers that sum to the target.
            Returns an empty list if no such pair is found.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                # LeetCode expects 1-based indexing for the output
                return [left + 1, right + 1]

        return []