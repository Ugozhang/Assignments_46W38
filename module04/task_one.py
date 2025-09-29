import MyModule 

x_i = MyModule.get_a_list_of_numbers()
x_min = MyModule.find_min(x_i)
x_max = MyModule.find_max(x_i)

print(x_i, x_min, x_max)
print(f"The list of number is: {[float(i) for i in x_i]}")
print(f"The minimal number is: {x_min:>5}")
print(f"The maximal number is: {x_max:>5}")