# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     if len(array)>2:
#         for i in range(len(array)):
#             for j in range(1,len(array)):
#                 sum = array[i]+array[j]
#                 if sum == targetSum:
#                     return [array[i], array[j]]
#     elif len(array)==2:
#         return [array[0], array[1]]
#     else:
#         return []


# O(n^2) time complex
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i+1, len(array)):
#             secNum = array[j]
#             if firstNum+secNum == targetSum:
#                 return [firstNum, secNum]


#O(n) time and O(n) space HASH TABLE

# def twoNumberSum(array, targetSum):
#     nums = {}
#     # x + y = targetSum
#     # y = targetSum - x
#     for num in array:
#         if targetSum - num in nums:          
#             return [num, targetSum-num]        
#         else:
#             nums[num] = True
    
#     return []

#O(nlog(n)) time and 0(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
    



array =[3, 5, -4, 8, 11, 1, -1, 6]
targetSum= 10
print(twoNumberSum(array,targetSum))

# array =[3, 5]
# targetSum= 8
# print(twoNumberSum(array,targetSum))

array=[4, 6, 1]
targetSum= 5
print(twoNumberSum(array,targetSum))
