def bubble_sort(unordered_list):
    n_iter = 0
    interchange=True
    while(interchange):
        n_iter += 1
        interchange = False
        for i in range(len(unordered_list) - 1):
            if unordered_list[i] > unordered_list[i + 1] :
                unordered_list[i], unordered_list[i + 1] = unordered_list[i + 1], unordered_list[i]
                interchange = True
    print(f"Bubble sort iterations {n_iter}")
    return unordered_list
