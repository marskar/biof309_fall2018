from copy import deepcopy
list1 = ["a", ["b", "c"]]
list2 = list1 # alias
list3 = list(list1) # shallow copy
list4 = deepcopy(list1) # deep copy

list1.append(4) # only added to list1 and 2
print(list1, list2, list3, list4, sep="\n")

list1[0] = 1 # only changed in list 1 and 2
print(list1, list2, list3, list4, sep="\n")

list1[1][0] = 2 # changed in lists 1, 2 and 3
print(list1, list2, list3, list4, sep="\n")


