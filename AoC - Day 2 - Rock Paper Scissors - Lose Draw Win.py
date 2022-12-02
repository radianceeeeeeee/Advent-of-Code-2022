total_score = 0

with open('input2.txt') as f:
    x = f.readlines()

    for i in x:
        opp = i[0]
        you = i[2]

        if opp == "A":
            if you == "X":
                score = 3
            elif you == "Y":
                score = 4
            else:
                score = 8
        elif opp == "B":
            if you == "X":
                score = 1
            elif you == "Y":
                score = 5
            else:
                score = 9
        else:
            if you == "X":
                score = 2
            elif you == "Y":
                score = 6
            else:
                score = 7

        total_score += score

print(total_score)