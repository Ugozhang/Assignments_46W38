# List Input function 
def get_a_list_of_numbers():
    
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
    # Input function till meeting "end" (Main)
    while str_input != "end":
        str_input = input("Input number (\"end\" for ending input)=>")
        if is_float(str_input):
            num_list.append(str_input)
        elif str_input != "end":
            print("Not a Number")
    return num_list

# min
def find_min(list_of_numbers):

    if len(list_of_numbers) == 0:
        print("No elements")
        return None
    else:
        # make min_index as pointer, while list[index]>list[i], index = i
        min_index_inlist = 0
        i=0
        while i<len(list_of_numbers):
            if float(list_of_numbers[i]) < float(list_of_numbers[min_index_inlist]):
                min_index_inlist = i
            i+=1
        return list_of_numbers[min_index_inlist]

# max
def find_max(list_of_numbers):

    if len(list_of_numbers) == 0:
        print("No elements")
        return None
    else:
        # make max_index as pointer, while list[index]>list[i], index = i
        max_index_inlist = 0
        i=0
        while i<len(list_of_numbers):
            if float(list_of_numbers[i]) > float(list_of_numbers[max_index_inlist]):
                max_index_inlist = i
            i+=1
        return list_of_numbers[max_index_inlist]
