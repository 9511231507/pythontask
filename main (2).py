keys=input("Enter keys separated by space: ").split()
num_lists=int(input("enter the number of value lists: "))
result_dict= {}
for i in range(num_lists):
    values=input(f"enter the values separated by space for{keys[i]}: ").split()
    resuli_dict[keys[i]]=values
print("\increated dictionary:")
print(result_dict)

