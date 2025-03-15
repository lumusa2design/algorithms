n_iter = 0

def merge_sort(lista):
    global n_iter
    if len(lista) > 1:
        n_iter +=1
        mid = len(lista)//2
        left = lista[0:mid]
        right = lista[mid:len(lista)]
        left = merge_sort(left)
        right = merge_sort(right)
        res =merge(left, right)
        return res
    return lista


def merge(left, right):
    global n_iter
    res = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        n_iter +=1
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return  res

def count_n_iter():
    return n_iter