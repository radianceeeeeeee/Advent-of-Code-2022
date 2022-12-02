dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

total_score = 0

with open('input2.txt') as f:
    x = f.readlines()

    for i in x:
        opp = i[0]
        you = i[2]

        score = 3 + dict[you]  # default to draw

        if opp == "A":
            if you == "Y":
                score = 6 + dict[you]    
            elif you == "Z":
                score = 0 + dict[you]
        elif opp == "B":
            if you == "X":
                score = 0 + dict[you]
            elif you == "Z":
                score = 6 + dict[you]
        else:
            if you == "X":
                score = 6 + dict[you]
            elif you == "Y":
                score = 0 + dict[you]

        total_score += score

print(total_score)