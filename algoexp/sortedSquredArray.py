#O(nlong n)
# def sortedSquaredArray(array):
#     squartedArray = []
#     for num in array:
#         squartedArray.append(num*num)
#     squartedArray.sort()
#     return squartedArray


# O(n) time complex

def sortedSquaredArray(array):
    squartedArray = [0 for _ in array]
    start = 0
    end = len(array) - 1
    i = len(array) - 1
    for _ in array:
        if abs(array[start]) > array[end]:
            squartedArray[i]= array[start]*array[start]
            i -= 1
            start += 1
        else:
            squartedArray[i] = array[end]*array[end]
            i -= 1
            end -= 1
    print(squartedArray)




values=[-2,-1,0,1,2,3]
sortedSquaredArray(values)

