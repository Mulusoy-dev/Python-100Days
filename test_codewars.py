
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]


input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

output = []
index = 0

for i in input:
    
    # print(i)
    for k in i:
        if k >= 50:
            output.insert(index, "Senior")
            break
        
        else:
            output.insert(index, "Open")
            break

    index += 1 

print(output)