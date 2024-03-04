def sort_array( _list = [] ):
    n = len(_list)
    for i in range(n):
        swapped = True
        for j in range(0, (n-i-1)):
            if _list[j] > _list[j+1]:
                _list[j], _list[j+1] = _list[j+1], _list[j]
                swapped = True
        if not swapped:
            break


my_list = [8, 9,0,3,6,3,11,4,7]
sort_array(my_list)
print(my_list)