class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return  self.frequency < other.frequency

def frequency_counter(text):
    frequencies = {}
    for character in text:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1
    return frequencies

def sort_nodes(list_of_nodes):
    for i in range(len(list_of_nodes)):
        min_index = i
        for j in range(i+1, len(list_of_nodes)):
            if list_of_nodes[j].frequency < list_of_nodes[min_index].frequency:
                min_index = j
        list_of_nodes[i], list_of_nodes[min_index] = list_of_nodes[min_index], list_of_nodes[i]
    return list_of_nodes

def huffman_tree_create(frequencies):
    nodes = [Node(symbol, frequency) for symbol, frequency in frequencies.items()]

    while len(nodes) > 1:
        nodes = sort_nodes(nodes)
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)

        new = Node(None, node1.frequency + node2.frequency)
        new.left = node1
        new.right = node2

        nodes.append(new)

    return nodes[0]

def code_generate(node, prefix="", codes = None ):
    if codes is None:
        codes = {}
    if node.symbol is not None:
        codes[node.symbol] = prefix
    else:
        code_generate(node.left, prefix + '0', codes)
        code_generate(node.right, prefix + '1', codes)
    return codes

encode = lambda texto, codes: ''.join(codes[c] for c in texto)

def decode(codified_string, tree):
    result = ""
    node = tree
    for bit in codified_string:
        if bit =="0":
            node = node.left
        else:
            node = node.right
        if node.symbol is not None:
            result += node.symbol
            node = tree
    return result

