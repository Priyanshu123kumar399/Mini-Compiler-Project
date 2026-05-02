# -------- Module 2+3 (Parser + AST) --------
expr = ""
pos = 0

def F():
    global pos, expr
    if pos < len(expr) and expr[pos] == '(':
        pos += 1
        node = E()
        if pos < len(expr) and expr[pos] == ')':
            pos += 1
            return node
        else:
            raise Exception("Missing )")

    elif pos < len(expr) and expr[pos].isdigit():
        value = int(expr[pos])
        pos += 1
        return value
    else:
        raise Exception("Invalid Character")


def T():
    global pos, expr
    node = F()
    while pos < len(expr) and expr[pos] == '*':
        op = expr[pos]
        pos += 1
        right = F()
        node = (op, node, right)
    return node


def E():
    global pos, expr
    node = T()
    while pos < len(expr) and expr[pos] == '+':
        op = expr[pos]
        pos += 1
        right = T()
        node = (op, node, right)
    return node


# -------- Module 4 (TAC) --------
temp_count = 1
tac = []

def generate_TAC(node):
    global temp_count, tac

    if isinstance(node, int):
        return str(node)

    op, left, right = node

    left_val = generate_TAC(left)
    right_val = generate_TAC(right)

    temp = f"t{temp_count}"
    temp_count += 1

    line = f"{temp} = {left_val} {op} {right_val}"
    tac.append(line)

    return temp


# -------- Module 5 (Optimizer) --------
def optimize_TAC(tac_lines):
    seen = {}
    optimized = []

    for line in tac_lines:
        if line not in seen:
            seen[line] = True
            optimized.append(line)

    return optimized


# -------- Module 6 (Main Compiler) --------
def mini_compiler():
    global expr, pos, tac, temp_count

    expr = input("Enter Expression: ")
    pos = 0
    tac = []
    temp_count = 1

    ast = E()

    if pos != len(expr):
        print("Invalid Expression")
        return

    print("\nAST:", ast)

    generate_TAC(ast)

    print("\nTAC:")
    for line in tac:
        print(line)

    optimized = optimize_TAC(tac)

    print("\nOptimized TAC:")
    for line in optimized:
        print(line)


# Run
mini_compiler()