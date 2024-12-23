class Solution(object):

    def toSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Iterate through the list and check for the two-sum pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return indices of the two numbers
        return []  # Return empty list if no solution exists


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter target: "))
    solution = Solution()
    result = solution.toSum(nums, target)
    print("Indices of numbers that sum to target:", result)


if __name__ == "__main__":
    main()
