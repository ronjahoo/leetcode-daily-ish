from typing import List

def fourSumFirst(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result

def fourSumSecond(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):

            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result

if __name__ == "__main__":
    nums1 = [1,0,-1,0,-2,2]
    target1 = 0
    nums2 = [2,2,2,2,2]
    target2 = 8

    print(fourSumFirst(nums1, target1))
    print(fourSumFirst(nums2, target2))

    print(fourSumSecond(nums1, target1))
    print(fourSumSecond(nums2, target2))

