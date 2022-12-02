max_cal = -1
sub_cal = 0

with open('input1.txt') as f:
    x = f.readlines()

    for i in x:
        if i != "\n":
            sub_cal += int(i)
        else:
            if max_cal < sub_cal:
                max_cal = sub_cal
            sub_cal = 0

print(max_cal)
