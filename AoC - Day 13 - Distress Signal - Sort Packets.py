packets = []

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


with open('input13.txt') as f:
    inp = f.readlines()

    for i in inp:
        if i != "\n":
            packets.append(eval(i.rstrip("\n")))


dividerIndex1 = 1
dividerIndex2 = 1

# how does this work?
# there is no need to sort as we only need to find the index of [[2]] and [[6]]
# this means that if [[2]] is greater to a packet, that will be its index
# same explanation for [[6]] but we have to add 1 because [[2]] < [[6]]

for i in packets:
    if nested_list_comparator(i, [[2]]) > -1:
        dividerIndex1 += 1

    if nested_list_comparator(i, [[6]]) > -1:
        dividerIndex2 += 1

print(dividerIndex1 * (dividerIndex2 + 1))