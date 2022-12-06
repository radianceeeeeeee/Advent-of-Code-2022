with open('input6.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        j = 0
        while j < len(i) - 14:
            if len(set(i[j:j+14])) == 14:
                print(j + 14)
                break
            j += 1
