arr = [2, 4, 5]
arr2 = [2, 3, 6]

def multiplyVectors(list, list2):
    multipliedList = []
    for i in range(0, len(list)):
        multipliedList.append(list[i] * list2[i])    
    return multipliedList

print(multiplyVectors(arr, arr2))





