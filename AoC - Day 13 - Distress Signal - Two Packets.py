def nested_list_comparator(list1: list, list2: list) -> int:
    """Checks the two lists if the values in the same index are the same
    - if first list has a smaller value or smaller length, return 1 -- packets are in order
    - if second list has a smaller value or smaller length, return -1 -- packets are not in order
    - if all values and lengths are equal, return 0 - check succeeding indices
    """
    i = 0
    minILength = min(len(list1), len(list2))

    while i < minILength:
        if isinstance(list1[i], int) and isinstance(list2[i], int):
            if list1[i] > list2[i]:
                return -1
            elif list1[i] < list2[i]:
                return 1

        elif isinstance(list1[i], list) and isinstance(list2[i], list):
            nest = nested_list_comparator(list1[i], list2[i])
            if nest == -1:
                return -1
            elif nest == 1:
                return 1
            
        elif isinstance(list1[i], int) and isinstance(list2[i], list):
            nest = nested_list_comparator([list1[i]], list2[i])
            if nest == -1:
                return -1
            elif nest == 1:
                return 1

        elif isinstance(list1[i], list) and isinstance(list2[i], int):
            nest = nested_list_comparator(list1[i], [list2[i]])
            if nest == -1:
                return -1
            elif nest == 1:
                return 1

        i += 1

    if len(list1) > len(list2):
        return -1
    elif len(list1) < len(list2):
        return 1

    return 0

sumIndices = 0

with open('input13.txt') as f:
    inp = f.readlines()

    i = 0

    while i < len(inp):
        val1 = inp[i]
        val2 = inp[i + 1]

        if nested_list_comparator(eval(val1), eval(val2)) > -1:
            sumIndices += (i // 3) + 1      # there are three lines per index so divide by three. add 1 because input is 1-based index

        i += 3      # 2 values + 1 newline = 3 lines

print(sumIndices)
