# Module 1: Lexical Analyzer in Python
KEYWORDS = {
    "int", "float", "char", "double", "long", "short",
    "if", "else", "while", "for", "do", "return",
    "break", "continue", "void"
}

MULTI_OPERATORS = {
    "==", "!=", "<=", ">=", "++", "--",
    "+=", "-=", "*=", "/=",
    "&&", "||"
}

SINGLE_OPERATORS = set("+-*/%=;(){}[]<>,!&|")


def is_identifier_start(ch):
    return ch.isalpha() or ch == "_"


def is_identifier_part(ch):
    return ch.isalnum() or ch == "_"


def tokenize(code):
    tokens = []
    i = 0
    n = len(code)

    while i < n:
        ch = code[i]

        # Skip whitespace
        if ch.isspace():
            i += 1
            continue

        # Skip single-line comments
        if ch == "/" and i + 1 < n and code[i + 1] == "/":
            i += 2
            while i < n and code[i] != "\n":
                i += 1
            continue

        # Multi-character operators
        if i + 1 < n and code[i:i + 2] in MULTI_OPERATORS:
            tokens.append((code[i:i + 2], "OPERATOR"))
            i += 2
            continue

        # Signed numbers (e.g., -42)
        if ch == "-" and i + 1 < n and code[i + 1].isdigit():
            j = i + 1
            while j < n and code[j].isdigit():
                j += 1
            tokens.append((code[i:j], "NUMBER"))
            i = j
            continue

        # Numbers
        if ch.isdigit():
            j = i
            while j < n and code[j].isdigit():
                j += 1
            tokens.append((code[i:j], "NUMBER"))
            i = j
            continue

        # Identifiers and Keywords
        if is_identifier_start(ch):
            j = i
            while j < n and is_identifier_part(code[j]):
                j += 1
            word = code[i:j]
            if word in KEYWORDS:
                tokens.append((word, "KEYWORD"))
            else:
                tokens.append((word, "IDENTIFIER"))
            i = j
            continue

        # Single-character operators
        if ch in SINGLE_OPERATORS:
            tokens.append((ch, "OPERATOR"))
            i += 1
            continue

        # Unknown token
        tokens.append((ch, "UNKNOWN"))
        i += 1

    return tokens

if __name__ == "__main__":
    print("Enter source code (Press Enter twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    source_code = "\n".join(lines)

    token_list = tokenize(source_code)

    print("\nTokens Generated:")
    for token, token_type in token_list:
        print(f"Token: {token} -> {token_type}")