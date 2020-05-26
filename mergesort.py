def merge_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        lefthalf = sort_list[:mid]
        righthalf = sort_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                sort_list[k] = lefthalf[i]
                i = i + 1
            else:
                sort_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            sort_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            sort_list[k] = righthalf[j]
            j = j + 1
            k = k + 1
