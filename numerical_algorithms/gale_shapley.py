def gale_shapley(prefA: dict[str, list[str]], prefB: dict[str, list[str]]) -> dict[str, str]:
    freeA = list(prefA.keys())
    freeB = list(prefB.keys())
    matches = {}
    proposals = {a: [] for a in prefA.keys()}

    while freeA:
        a = freeA[0]
        a_pref_list = prefA[a]
        for b in a_pref_list:
            if b not in proposals[a]:
                proposals[a].append(b)
                if b not in matches.values():
                    matches[a] = b
                    freeA.remove(a)
                    break
                else:
                    current_a = [key for key, value in matches.items() if value == b][0]
                    b_pref_list = prefB[b]
                    if b_pref_list.index(a) < b_pref_list.index(current_a):
                        matches[a] = b
                        freeA.remove(a)
                        freeA.append(current_a) 
                        del matches[current_a]
                        break
        else:
            freeA.remove(a)

    return matches
