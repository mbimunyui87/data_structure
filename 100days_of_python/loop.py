mylist = [ 120, 145, 105, 98 ]
i = 0 
t = 0
for n in mylist:
    n = i + n
    i = n
    t += 1
print(f'Total sum is {n} ' )
print(f'the average hieght is {n/t}')

def max(mylist = []):
    max = 0
    for n in mylist:
        if n > max:
            max = n
    print(f'Max number is {max}')

def sum_of_even(n):
    sum = 0
    for i in range(1, n+1 ):
        if i%5 == 0 :
            sum += i
            print(i)
    return sum


scores = [12, 14, 10, 9, 18, 17, 12 ]
max(scores)
print('the sum function \n')
print(sum_of_even(100))


