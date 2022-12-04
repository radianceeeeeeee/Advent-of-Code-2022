dict_upper = {chr(x): x - 64 + 26 for x in range (65, 91)}
dict_lower = {chr(x): x - 96 for x in range(97, 123)}

total_priority = 0

with open('input3.txt') as f:
    inp = f.readlines()
    elf = 1
    same_letters = set()

    for line in inp:
        if elf == 1:
            same_letters = set(list(line))
            elf += 1
        elif elf == 2:
            same_letters = same_letters.intersection(set(list(line.rstrip('\n'))))
            elf += 1
        else:
            same_letters = same_letters.intersection(set(list(line.rstrip('\n'))))
            x = same_letters.pop()              # NOTE: same_letters is guaranteed to contain 1 element due to problem specs

            if x in dict_upper.keys():
                total_priority += dict_upper[x]
            else:
                total_priority += dict_lower[x]
            
            same_letters.clear()
            elf = 1

        
print(total_priority)

