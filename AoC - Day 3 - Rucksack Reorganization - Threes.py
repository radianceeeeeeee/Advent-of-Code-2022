dict_upper = {chr(x): x - 64 + 26 for x in range (65, 91)}
dict_lower = {chr(x): x - 96 for x in range(97, 123)}

total_priority = 0

def find_same_letter(arr):
    for i in arr[0]:
        for j in arr[1]:
            for k in arr[2]:
                if i == j and j == k:
                    return i

with open('input3.txt') as f:
    inp = f.readlines()
    elf = 0
    sacks = []
    for line in inp:
        elf += 1
        sacks.append(line)
        if elf == 3:
            x = find_same_letter(sacks)

            if x in dict_upper.keys():
                total_priority += dict_upper[x]
            else:
                total_priority += dict_lower[x]

            elf = 0
            sacks = []
        
print(total_priority)

