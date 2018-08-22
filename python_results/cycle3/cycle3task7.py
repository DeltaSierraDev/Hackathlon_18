num_input = input()
num_list = num_input.split(" ")
result_str = ""

for x in num_list:
    if x[0]== "-":
        result_str += "-"
    else :
        result_str += "+"

print(result_str[1:])
