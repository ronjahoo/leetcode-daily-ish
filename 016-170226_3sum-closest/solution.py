from typing import List

def threeSumClosestFirst(nums: List[int], target: int) -> int:
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                return total

            elif total < target:
                if abs(total - target) < abs(closest - target):
                    closest = total
                left += 1
            else:
                if abs(total - target) < abs(closest - target):
                    closest = total
                right -= 1

    return closest

def threeSumClosestSecond(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)

    closest_diff = float("inf")

    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            diff = total - target

            if abs(diff) < abs(closest_diff):
                closest_diff = diff

            if diff < 0:
                left += 1
            elif diff > 0:
                right -= 1
            else:
                return target

    return target + closest_diff

if __name__ == "__main__":
    nums1 = [-1,2,1,-4]
    target1 = 1
    nums2 = [0,0,0]
    target2 = 1

    print(threeSumClosestFirst(nums1, target1))
    print(threeSumClosestFirst(nums2, target2))

    print(threeSumClosestSecond(nums1, target1))
    print(threeSumClosestSecond(nums2, target2))

