def sort(array) :
    tmp = 0
    for i in range(0, n):
        j = i - 1
        while (j >= 0) and (array[j] > array[j+1]) :
            tmp = array[j]
            array[j] = array[j+1]
            array[j+1] = tmp
            j -= 1

n = int(input())
my_list = [int(el) for el in input().split()]
sort(my_list)
for i in range(0, n):
    print(my_list[i], end = ' ')
