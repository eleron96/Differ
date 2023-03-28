import json
import yaml
import os


def load_data(file_path):
    _, ext = os.path.splitext(file_path)

    with open(file_path, 'r') as file:
        if ext == '.json':
            return json.load(file)
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {ext}")


def format_value(value, indent_level, indent):
    if isinstance(value, dict):
        return format_dict(value, indent_level + 1, indent)
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_dict(d, indent_level, indent):
    lines = []
    for key, value in d.items():
        lines.append(f'{indent * (indent_level + 1)}{key}: {format_value(value, indent_level + 1, indent)}')
    return '{\n' + '\n'.join(lines) + f'\n{indent * indent_level}' + '}'


def compare_dicts(d1, d2, indent_level, indent):
    def compare_dicts_rec(d1, d2, keys, indent_level, indent):
        if not keys:
            return []
        key = keys[0]
        result = []
        if key in d1 and key in d2:
            result.extend(handle_both_keys(d1, d2, key, indent_level, indent))
        elif key in d1:
            result.extend(handle_key_in_d1(d1, key, indent_level, indent))
        else:
            result.extend(handle_key_in_d2(d2, key, indent_level, indent))
        return result + compare_dicts_rec(d1, d2, keys[1:], indent_level, indent)

    keys = sorted(set(d1.keys()).union(d2.keys()))
    return compare_dicts_rec(d1, d2, keys, indent_level, indent)


def handle_both_keys(d1, d2, key, indent_level, indent):
    result = []

    if d1[key] == d2[key]:
        result.append(indent * indent_level + f'  {key}: {format_value(d1[key], indent_level, indent)}')
    elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
        result.append(indent * indent_level + f'  {key}:')
        result.extend(compare_dicts(d1[key], d2[key], indent_level + 1, indent))
    else:
        result.append(indent * indent_level + f'- {key}: {format_value(d1[key], indent_level, indent)}')
        result.append(indent * indent_level + f'+ {key}: {format_value(d2[key], indent_level, indent)}')

    return result

def handle_key_in_d1(d1, key, indent_level, indent):
    return [indent * indent_level + f'- {key}: {format_value(d1[key], indent_level, indent)}']

def handle_key_in_d2(d2, key, indent_level, indent):
    return [indent * indent_level + f'+ {key}: {format_value(d2[key], indent_level, indent)}']

def compare_files_stylish(file_path1, file_path2):
    d1 = load_data(file_path1)
    d2 = load_data(file_path2)
    result_lines = compare_dicts(d1, d2, 1, '  ')
    return '{\n' + '\n'.join(result_lines) + '\n}'


