def insert_sort(_list):
    for i in range(1, len(_list)):
        key = _list[i]
        j = i - 1
        while j >= 0 and key < _list[j]:
            _list[j+1] = _list[j]
            j -= 1
        _list[j + 1] = key
my_list = [3,9,5,7,1,3,6,15,20]
insert_sort(my_list)
print(my_list)