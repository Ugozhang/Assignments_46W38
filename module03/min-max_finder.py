
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
