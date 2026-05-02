temp_count = 1

def generate_TAC(node):
    global temp_count

   
    if isinstance(node, int):
        return str(node)

    # अगर operator node है
    op, left, right = node

    left_val = generate_TAC(left)
    right_val = generate_TAC(right)

    temp = f"t{temp_count}"
    temp_count += 1

    print(f"{temp} = {left_val} {op} {right_val}")

    return temp