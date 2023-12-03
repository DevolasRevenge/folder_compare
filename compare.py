import os

path1 = "put absolute path here"
pc_list = os.listdir(path1)
print(pc_list)

path2 = "put absolute path here"
switch_list = os.listdir(path2)
print(switch_list)


difference = []
for element in switch_list:
    if element not in pc_list:
        difference.append(element)

for i in range(5):
    print("\n") 
print(*difference,sep='\n')