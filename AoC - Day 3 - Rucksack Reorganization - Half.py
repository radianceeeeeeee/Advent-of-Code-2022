dict_upper = {chr(x): x - 64 + 26 for x in range (65, 91)}
dict_lower = {chr(x): x - 96 for x in range(97, 123)}

total_priority = 0

with open('input3.txt') as f:
    inp = f.readlines()

    for line in inp:
        c1 = set(list(line[:len(line)//2]))
        c2 = set(list(line[len(line)//2:]))

        same_letters = c1.intersection(c2)
        x = same_letters.pop()              # NOTE: same_letters is guaranteed to contain 1 element due to problem specs

        if x in dict_upper.keys():
            total_priority += dict_upper[x]
        else:
            total_priority += dict_lower[x]

print(total_priority)

