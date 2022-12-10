x = 1
cycleNum = 0
screenCRT = []

def pixel_brightness(cycle, reg):
    pixelPos = cycle % 40 + 1   # offset cycleNum by 1
    if 0 <= pixelPos - reg <= 2 and reg + 1 >= 0:   # since cycleNum is offset by 1, offset reg value by 1 too
        return "#"
    return "."

def print_screen(screen):
    i = 0
    while i < len(screen):
        if i % 40 == 0:     # 40 is the screen width
            print()
        print(screen[i], end = "")
        i += 1

with open('input10.txt') as f:
    inp = f.readlines()

    for i in inp:
        command = i.split()

        screenCRT.append(pixel_brightness(cycleNum, x))
        cycleNum += 1       # one cycle delay for both noop and addx

        if command[0] == "addx":
            screenCRT.append(pixel_brightness(cycleNum, x))
            cycleNum += 1       # another cycle delay for addx

            x += int(command[1])


print_screen(screenCRT)