nx = input()
nx_list = nx.split(" ")
N = int(nx_list[0])
X = int(nx_list[1])
h_str = input()
height_list = h_str.split(" ")
sum = 0
result = 0

i = 0
while i < (N-1):
    sum += int(height_list[i])
    i += 1

if sum < X:
    result = X - sum
    print(result)
