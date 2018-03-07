arr1 = [1, 3, 2, 4]
arr2 = [5, 2, 1, 0]


def addVectors(arr1, arr2):
    addList = []
    for i in range(0, len(arr1)):
        addList.append(arr1[i] + arr2[i])    
    return addList

print(addVectors(arr1, arr2))