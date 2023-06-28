# 4)	Write a python program to find the second largest element in an array without using sort function.
arr = [1,2,4,10,9]
def second_big(arr):
    second_max = 0
    max = 0
    for num in arr:
        if num >max:
            second_max = max
            max = num
        elif num>second_max and num<max:
            second_max =num
    return second_max
res = second_big(arr)
print(res)