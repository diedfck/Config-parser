import re
from collections import deque

def evaluate_postfix(expression, variables):
    stack = deque()
    operators = {'+': lambda x, y: x + y, '*': lambda x, y: x * y, '-': lambda x, y: x - y, 'ord': ord, 'pow': pow}

    for token in expression:
        if token in operators:
            if token == 'ord':
                operand = stack.pop()
                if isinstance(operand, str) and len(operand) == 1:
                    stack.append(operators[token](operand))
                elif isinstance(operand, str) and len(operand) > 1:
                    raise ValueError(f"ord() ожидает строку длиной 1, но найден {operand}")
                else:
                    raise ValueError(f"ord() ожидает строку, но найден {type(operand)} с значением {operand}")
            elif token == 'pow':
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов для pow()")
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](x, y))
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](x, y))
        else:
            if token in variables:
                stack.append(variables[token])
            elif token.isdigit():
                stack.append(int(token))
            else:
                raise ValueError(f"Неизвестная переменная или некорректный операнд: {token}")

    return stack.pop()


def process_config(input_file, output_file):
    variables = {}
    output_lines = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            if line.startswith('\\'):
                continue

            match = re.match(r'set\s+(\w+)\s*=\s*(.+);', line)
            if match:
                name, value = match.groups()

                if value.startswith('[') and value.endswith(']'):
                    elements = value[1:-1].split(';')
                    elements = [int(e) if e.isdigit() else f'"{e}"' for e in elements]
                    output_lines.append(f'{name} = [{", ".join(map(str, elements))}]')
                elif value.startswith('"') and value.endswith('"'):
                    output_lines.append(f'{name} = {value}')
                    variables[name] = value.strip('"')
                elif re.match(r'[\w\s+*\-ordpow]+', value):
                    postfix_tokens = value.split()
                    try:
                        result = evaluate_postfix(postfix_tokens, variables)
                        variables[name] = result
                        output_lines.append(f'{name} = {result}')
                    except Exception as e:
                        output_lines.append(f'Ошибка в вычислении {name}: {e}')
                elif value in variables:
                    variables[name] = variables[value]
                    output_lines.append(f'{name} = {variables[name]}')
                else:
                    variables[name] = int(value)
                    output_lines.append(f'{name} = {value}')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(output_lines))

input_file = 'input.txt'
output_file = 'output.toml'
process_config(input_file, output_file)
