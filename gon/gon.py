import os
from typing import List


def is_symbol(c: str) -> bool:
    return c == '=' or c == ',' or c == ':' or c == '{' or c == '}' or c == '[' or c == ']'


def is_symbol_ignored(c: str) -> bool:
    return c == '=' or c == ',' or c == ':'


def is_whitespace(c: str) -> bool:
    return c == ' ' or c == '\n' or c == '\r' or c == '\t'


def tokenize(filename: str, data: str) -> ...:
    tokens: List[str] = []

    current_token = ''
    
    is_string_data = False
    is_comment = False

    for char in data:
        if is_comment:
            if char == '\n':
                is_comment = False
            continue

        if not is_string_data:
            if is_symbol(char):
                if current_token != '':
                    tokens.append(current_token)
                    current_token = ''

                if not is_symbol_ignored(char):
                    current_token += char
                    tokens.append(current_token)
                    current_token = ''

                continue

            if is_whitespace(char):
                if current_token != '':
                    tokens.append(current_token)
                    current_token = ''
                continue
            
            if char == '"':
                if current_token != '':
                    tokens.append(current_token)
                    current_token = ''
                is_string_data = True
                continue

            if char == '#':
                if current_token != '':
                    tokens.append(current_token)
                    current_token = ''
                is_comment = True 
                continue
        else:
            if char == '"':
                tokens.append(current_token)
                current_token = ''
                is_string_data = False
                continue

        current_token += char

    if current_token != "":
        tokens.append(current_token)

    return tokens

        


def load(filename: str) -> ...:  # TODO: tokens
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Gon file does not exists in path { filename }")

    with open(filename, 'r', encoding="utf-8") as file:
        tokens = tokenize(filename, file.read())

        print(tokens)


if __name__ == "__main__":
    load("./test.txt")




