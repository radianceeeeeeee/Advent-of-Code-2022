total_fully_contained = 0

with open('input4.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        elf1str, elf2str = i.split(",")
        elf1tpl = tuple(map(int, elf1str.split("-")))
        elf2tpl = tuple(map(int, elf2str.split("-")))

        elf1 = set(range(elf1tpl[0], elf1tpl[1] + 1))
        elf2 = set(range(elf2tpl[0], elf2tpl[1] + 1))

        if elf1.issubset(elf2) or elf2.issubset(elf1):
           total_fully_contained += 1

print(total_fully_contained)