#  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    p = nums[:]
    p.sort() #sorting in -> O(nlogn)
    r = len(nums)-1
    l =0 

    #find the indices -> O(n)
    for i in range(len(nums)):
      if(p[l] + p[r]<target): 
        l += 1
      elif (p[l] + p[r]>target): 
        r -=1
      else :
        first_num = p[l]
        second_num = p[r]

    #find the indices of the numbers -> O(n)
    for i in range(len(nums)):
      if(nums[i]==first_num):
        first_index = i
      elif (nums[i]==second_num):
        second_index = i
    return [first_index+1,second_index+1]