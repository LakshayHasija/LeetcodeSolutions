class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1=list(map(int,version1.split(".")))
        nums2=list(map(int,version2.split(".")))
        
        maxlen=max(len(nums1),len(nums2))
        nums1.extend([0]*(maxlen-len(nums1)))
        nums2.extend([0]*(maxlen-len(nums2)))

        for i in range(len(nums1)):
            if nums1[i]>nums2[i]:
                return 1
            if nums1[i]<nums2[i]:
                return -1
        return 0