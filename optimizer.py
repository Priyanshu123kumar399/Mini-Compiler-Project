def optimize_TAC(tac_lines):
    seen = {}
    optimized = []

    for line in tac_lines:
        if line in seen:
            continue
        seen[line] = True
        optimized.append(line)

    return optimized