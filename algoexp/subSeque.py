def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0
    for num in array:
        if num == sequence[0+j]:
            if len(sequence)-1 == j:
                return True
            j += 1
            
    return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array,sequence))