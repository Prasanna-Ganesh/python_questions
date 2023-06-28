#5)	Write a python program to create a list having 5 elements. Find the smallest number and the largest number and swap them.

list1=[1,2,3,4,5]
min_value = min(list1)
max_value = max(list1)

smallind=list1.index(min_value)
biginind=list1.index(max_value)

list1[smallind]= max_value
list1[biginind]= min_value
print(list1)