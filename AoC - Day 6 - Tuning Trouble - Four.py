with open('input6.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        j = 0
        while j < len(i) - 4:
            if len(set(i[j:j+4])) == 4:
                print(j + 4)
                break
            j += 1
