dict_upper = {chr(x): x - 64 + 26 for x in range (65, 91)}
dict_lower = {chr(x): x - 96 for x in range(97, 123)}

total_priority = 0

def find_same_letter(str1, str2):
    for i in str1:
        for j in str2:
            if i == j:
                return i


with open('input3.txt') as f:
    inp = f.readlines()

    for line in inp:
        c1 = line[:len(line)//2]
        c2 = line[len(line)//2:]

        x = find_same_letter(c1, c2)

        if x in dict_upper.keys():
            total_priority += dict_upper[x]
        else:
            total_priority += dict_lower[x]

print(total_priority)

