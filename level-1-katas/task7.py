def combine(list1, list2):
    new_list =[]

    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        new_list.append((list1[i], list2[i]))

    return new_list


print(combine([11,22,33,45], [1,2,3]))