from data_structures.binary_tree import Node, BinaryTree


def menu_to_binary(menu_dict):
    root = Node("__ROOT__")

    def chain(items):
        first = prev = None
        for name, sub in items:
            node = Node(name)
            if first is None:
                first = node
            if prev:
                prev.right_son = node
            prev = node
            if isinstance(sub, dict) and sub:
                node.left_son = chain(list(sub.items()))
        return first

    root.left_son = chain(list(menu_dict.items()))
    return BinaryTree(root)


def menu_preorder(root):
    start = root.left_son if getattr(root, "value", None) == "__ROOT__" else root
    def pre(n):
        if not n: return
        yield n
        yield from pre(n.left_son)
        yield from pre(n.right_son)
    yield from pre(start)


def menu_find_path(root, path):
    n = root.left_son if getattr(root, "value", None) == "__ROOT__" else root
    for name in path:
        cur = n
        found = None
        while cur:
            if cur.value == name:
                found = cur
                break
            cur = cur.right_son
        if not found:
            return None
        n = found.left_son
    return found


def _tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isspace():
            i += 1
        elif c.isdigit() or c == '.':
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            tokens.append(expr[i:j])
            i = j
        elif c.isalpha():
            j = i
            while j < len(expr) and expr[j].isalnum():
                j += 1
            tokens.append(expr[i:j])
            i = j
        elif c in "+-*/^()":
            tokens.append(c)
            i += 1
        else:
            raise ValueError(f"Carácter no válido: {c}")
    return tokens


def _to_rpn(tokens):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_son_assoc = {'^'}
    output, stack = [], []
    for t in tokens:
        if t.replace('.', '', 1).isdigit() or t.isalpha():
            output.append(t)
        elif t in prec:
            while stack and stack[-1] in prec and (
                (stack[-1] not in right_son_assoc and prec[stack[-1]] >= prec[t]) or
                (stack[-1] in right_son_assoc and prec[stack[-1]] > prec[t])
            ):
                output.append(stack.pop())
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Paréntesis desbalanceados")
            stack.pop()
        else:
            raise ValueError(f"Token inesperado: {t}")
    while stack:
        if stack[-1] in '()':
            raise ValueError("Paréntesis desbalanceados")
        output.append(stack.pop())
    return output


def expression_to_tree(expr):
    tokens = _tokenize(expr)
    rpn = _to_rpn(tokens)
    st = []
    for t in rpn:
        if t in "+-*/^":
            b = st.pop()
            a = st.pop()
            node = Node(t)
            node.left_son = a
            node.right_son = b
            st.append(node)
        else:
            val = float(t) if t.replace('.', '', 1).isdigit() else t
            st.append(Node(val))
    if len(st) != 1:
        raise ValueError("Expresión inválida")
    return BinaryTree(st[0])


def eval_expr_tree(node, env=None):
    env = env or {}
    if node.left_son is None and node.right_son is None:
        if isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node.value, str):
            if node.value in env:
                return float(env[node.value])
            raise KeyError(f"Variable '{node.value}' no definida")
    ops = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b,
        '^': lambda a,b: a**b
    }
    if node.value in ops:
        return ops[node.value](eval_expr_tree(node.left_son, env),
                             eval_expr_tree(node.right_son, env))
    raise ValueError("Nodo desconocido en árbol de expresión")

expr_tree = expression_to_tree("3 + 4 * 2 / (1 - 5)^2")
print("Resultado:", eval_expr_tree(expr_tree.root))

expr_tree2 = expression_to_tree("x^2 + 2*x + 1")
print("Resultado con x=3:", eval_expr_tree(expr_tree2.root, {"x": 3}))
