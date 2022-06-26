def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secNum = array[j]
            if firstNum+secNum == targetSum:
                return [firstNum, secNum]

    return []
array=[4,1]
targetSum= 5
print(twoNumberSum(array,targetSum))