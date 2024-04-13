def find_median_sorted_arrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n % 2 == 0:
        return (nums1[n // 2 - 1] + nums1[n // 2]) / 2
    else:
        return nums1[n // 2]

n1 = [11,21,2,50]
n2 = [1,12,3,4,5]
print("The Median is:", find_median_sorted_arrays(n1,n2))

