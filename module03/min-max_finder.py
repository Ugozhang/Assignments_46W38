
# Number_Validation_byFloat
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# var_declaration
num_list = []
str_input = ""

# Input function (Main)
while str_input != "end":
    str_input = input("Input number (\"end\" for ending input)=>")
    if is_float(str_input):
        num_list.append(str_input)
    elif str_input != "end":
        print("Not a Number")

#Comparison for maximum and minimum
max_inlist = num_list[0]
min_inlist = num_list[0]
i=0
while i<len(num_list):
    if float(num_list[i]) > float(max_inlist):
        max_inlist = num_list[i]
    if float(num_list[i]) < float(min_inlist):
        min_inlist = num_list[i]
    i+=1

# Output
print("The list of number is:", num_list)
print("The minimal number is:", min_inlist)
print("The maximal number is:", max_inlist)

# sorting
def QuickSort_byBFC_asc(s):
    n = len(s)
    if n<=1:
        return s
    left=[]
    right=[]
    pivot = float(s[0])
    for i in range(1,n):
        if float(s[i]) < float(pivot):
            left.append(s[i])
        else:
            right.append(s[i])
    return QuickSort_byBFC_asc(left) + [pivot] + QuickSort_byBFC_asc(right)
def QuickSort_byBFC_dsc(s):
    n = len(s)
    if n<=1:
        return s
    left=[]
    right=[]
    pivot = float(s[0])
    for i in range(1,n):
        if float(s[i]) > float(pivot):
            left.append(s[i])
        else:
            right.append(s[i])
    return QuickSort_byBFC_dsc(left) + [pivot] + QuickSort_byBFC_dsc(right)
#while sorted list <> nan
list_sorted = []
while len(list_sorted) == 0:
    sortby_boolean = input("Sorting List by Asceding(True), or descending(False)? =>")
    if sortby_boolean == "1" or sortby_boolean == "True" or sortby_boolean == "true" or sortby_boolean == "T" or sortby_boolean == "t":
        list_sorted = QuickSort_byBFC_asc(num_list)
    elif sortby_boolean == "0" or sortby_boolean == "False" or sortby_boolean == "false" or sortby_boolean == "F" or sortby_boolean == "f":
        list_sorted = QuickSort_byBFC_dsc(num_list)
    else:
        print("Wrong typing")

print("The list of number sorted:", list_sorted)