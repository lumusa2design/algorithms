def trie_construction(words):
    trie = {}
    for word in words:
        current_dict = trie
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["*"] = "*"
    return trie
