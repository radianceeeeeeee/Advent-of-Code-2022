max_cal = [-3, -2, -1]
sub_cal = 0

with open('input1.txt') as f:
    x = f.readlines()

    for i in x:
        if i != "\n":
            sub_cal += int(i)
        else:
            if max_cal[0] < sub_cal:
                if max_cal[1] < sub_cal:
                    if max_cal[2] < sub_cal:
                        max_cal[0] = max_cal[1]
                        max_cal[1] = max_cal[2]
                        max_cal[2] = sub_cal
                    else:
                        max_cal[0] = max_cal[1]
                        max_cal[1] = sub_cal
                else:
                    max_cal[0] = sub_cal
            sub_cal = 0


print(max_cal[0] + max_cal[1] + max_cal[2])
