expr = ""
pos = 0

def F():
    global pos, expr
    if pos < len(expr) and expr[pos] == '(':
        pos += 1
        value = E()
        if pos < len(expr) and expr[pos] == ')':
            pos += 1
            return value
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
    value = F()
    while pos < len(expr) and expr[pos] == '*':
        pos += 1
        value = value * T()
    return value

def E():
    global pos, expr
    value = T()
    while pos < len(expr) and expr[pos] == '+':
        pos += 1
        value = value + E()
    return value

expr = input("Enter Expression: ")
pos = 0
result = E()

if pos != len(expr):
    print("Invalid Expression")
else:
    print("Result =", result)