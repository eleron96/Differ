import json
import yaml


def compare_dicts(d1, d2, indent_level, indent):
    result = []
    keys = sorted(set(d1.keys()).union(d2.keys()))

    for key in keys:
        if key in d1 and key in d2:
            result.extend(handle_both_keys(d1, d2, key, indent_level, indent))
        elif key in d1:
            result.extend(handle_key_in_d1(d1, key, indent_level, indent))
        elif key in d2:
            result.extend(handle_key_in_d2(d2, key, indent_level, indent))

    return result


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def handle_both_keys(d1, d2, key, indent_level, indent):
    result = []
    indent_str = ' ' * (indent * indent_level)

    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        result.append(f"{indent_str}{key}: {{")
        result.extend(compare_dicts(d1[key], d2[key], indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    elif format_value(d1[key]) != format_value(d2[key]):
        result.append(f"{indent_str}- {key}: {format_value(d1[key])}")
        result.append(f"{indent_str}+ {key}: {format_value(d2[key])}")
    else:
        result.append(f"{indent_str}  {key}: {format_value(d1[key])}")

    return result


def handle_key_in_d1(d1, key, indent_level, indent):
    result = []
    indent_str = ' ' * (indent * indent_level)

    if isinstance(d1[key], dict):
        result.append(f"{indent_str}- {key}: {{")
        result.extend(compare_dicts(d1[key], {}, indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    else:
        result.append(f"{indent_str}- {key}: {format_value(d1[key])}")

    return result


def handle_key_in_d2(d2, key, indent_level, indent):
    result = []
    indent_str = ' ' * (indent * indent_level)

    if isinstance(d2[key], dict):
        result.append(f"{indent_str}+ {key}: {{")
        result.extend(compare_dicts({}, d2[key], indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    else:
        result.append(f"{indent_str}+ {key}: {format_value(d2[key])}")

    return result


def load_file(file_path):
    with open(file_path) as f:
        if file_path.endswith('.json'):
            return json.load(f)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(f)
        else:
            raise ValueError("Unsupported file format")


def compare_files_stylish(file1, file2, indent=4):
    j_file1 = load_file(file1)
    j_file2 = load_file(file2)

    result = compare_dicts(j_file1, j_file2, 0, indent)
    return '\n'.join(result)
