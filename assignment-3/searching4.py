"""
Searching Exercise 4: Median of Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).. You may assume nums1 and nums2 cannot be both empty.

For Example:
nums1 = [1, 2], nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
def findMedianSortedArrays(nums1, nums2):
        # edge cases empty arrays
        if not nums1:
            return nums2[len(nums2)//2] if len(nums2)%2!=0 else (nums2[len(nums2)//2]+nums2[len(nums2)//2-1])/2
        if not nums2:
            return nums1[len(nums1)//2] if len(nums1)%2!=0 else (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        
        # edge cases one array strictly greater
        if nums1[0]>nums2[-1]:
            comb = nums2 + nums1
            return comb[len(comb)//2] if len(comb)%2!=0 else (comb[len(comb)//2]+comb[len(comb)//2-1])/2
        if nums2[0]>nums1[-1]:
            comb = nums1 + nums2
            return comb[len(comb)//2] if len(comb)%2!=0 else (comb[len(comb)//2]+comb[len(comb)//2-1])/2
            
        
        #return l and r index after cut
        def cut(arr,left,right):
            #even length
            if (left+right)%2 != 0:
                return (left+right)//2,(left+right)//2+1
            else:
                return (left+right)//2,(left+right)//2
            
        l1,r1 = cut(nums1,0,len(nums1)-1)
        l2,r2 = cut(nums2,0,len(nums2)-1)
        #print("l1 {},r1 {},l2 {},r2 {}".format(l1,r1,l2,r2))
            
        #while some numbers on the 2 left halfs are greater than numbers on the 2 right halfs
        while (nums1[l1]>nums2[r2] or nums2[l2]>nums1[r1]) and (l1!=r1 or l2 !=r2):
            if nums1[l1]>nums2[r2]:
                if l1 ==r1:
                    l2,r2 = cut(nums2,l2+1,len(nums2)-1)
                else:
                    l1,r1 = cut(nums1,0,l1)
            elif nums2[l2]>nums1[r1]:
                if l2 ==r2:
                    l1,r1 = cut(nums1,l1+1,len(nums1)-1)
                else:
                    l2,r2 = cut(nums2,0,l2)
        left = max(nums1[l1],nums2[l2])
        right = min(nums1[r1],nums2[r2])
        print('left:{},right:{}'.format(left,right))
        print("l1 {},r1 {},l2 {},r2 {}".format(l1,r1,l2,r2))
        return ((left+right)/2)

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1,nums2))