class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        def findFirst():
            left = 0
            right = n - 1
            idx = -1 

            while(left <= right):
                mid = (left + right) // 2

                if(target > nums[mid]):
                    left = mid + 1
                
                elif(target < nums[mid]):
                    right = mid - 1
                
                else:
                    idx = mid
                    right = mid - 1
            
            return idx

        def findLast():
            n = len(nums)
            left = 0
            right = n - 1
            idx = -1

            while(left <= right):
                mid = (left + right) // 2

                if(target > nums[mid]):
                    left = mid + 1
                
                elif(target < nums[mid]):
                    right = mid - 1

                else :
                    idx = mid
                    left = mid + 1
            
            return idx

        return[findFirst(), findLast()]