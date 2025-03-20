class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store the complement and its index
        complement_map = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in complement_map:
                # Return the indices of the complement and the current number
                return [complement_map[complement], i]

            # If complement not found, store the number and its index
            complement_map[num] = i
