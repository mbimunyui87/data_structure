
def selec_sort(_arr=[]):
   
    for i in range((len(_arr))):
        min_index = i
        for j in range(i+1, len(_arr)):
            if _arr[j] < _arr[min_index]:
                min_index = j
                
        _arr[i], _arr[min_index] = _arr[min_index], _arr[i]
    return _arr

my_list = [64, 35, 12, 22, 11]
result = selec_sort(my_list)
print(result)