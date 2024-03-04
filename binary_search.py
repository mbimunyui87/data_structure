def _list(mylist = [], target = None):
    left = 0
    right = len(mylist) - 1
    mid =  right/2
    while left <= right:
        print(mid)
        print(mylist[mid])
        if mylist[mid] == target:
            return mid
        elif mid < target:
            left = mid - 1
            mid = (left + right)/2
        else:
            right = mid - 1
            mid = (left + right)/2
        return -1
   
my_list = [4,5,1,20,16,4]
result = _list(my_list, 20)


