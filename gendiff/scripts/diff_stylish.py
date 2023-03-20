# import json
#
#
# def compare_dicts(d1, d2, indent_level, indent):
#     result = []
#     keys = sorted(set(d1.keys()).union(d2.keys()))
#
#     for key in keys:
#         if key in d1 and key in d2:
#             result.extend(handle_both_keys(d1, d2, key, indent_level, indent))
#         elif key in d1:
#             result.extend(handle_key_in_d1(d1, key, indent_level, indent))
#         elif key in d2:
#             result.extend(handle_key_in_d2(d2, key, indent_level, indent))
#
#     return result
#
#
# def handle_both_keys(d1, d2, key, indent_level, indent):
#     result = []
#     indent_str = ' ' * (indent * indent_level)
#
#     if isinstance(d1[key], dict) and isinstance(d2[key], dict):
#         result.append(f"{indent_str}{key}: {{")
#         result.extend(compare_dicts(d1[key], d2[key], indent_level + 1, indent))
#         result.append(f"{indent_str}}}")
#     elif d1[key] != d2[key]:
#         result.append(f"{indent_str}- {key}: {d1[key]}")
#         result.append(f"{indent_str}+ {key}: {d2[key]}")
#     else:
#         result.append(f"{indent_str}  {key}: {d1[key]}")
#
#     return result
#
#
# def handle_key_in_d1(d1, key, indent_level, indent):
#     result = []
#     indent_str = ' ' * (indent * indent_level)
#
#     if isinstance(d1[key], dict):
#         result.append(f"{indent_str}- {key}: {{")
#         result.extend(compare_dicts(d1[key], {}, indent_level + 1, indent))
#         result.append(f"{indent_str}}}")
#     else:
#         result.append(f"{indent_str}- {key}: {d1[key]}")
#
#     return result
#
#
# def handle_key_in_d2(d2, key, indent_level, indent):
#     result = []
#     indent_str = ' ' * (indent * indent_level)
#
#     if isinstance(d2[key], dict):
#         result.append(f"{indent_str}+ {key}: {{")
#         result.extend(compare_dicts({}, d2[key], indent_level + 1, indent))
#         result.append(f"{indent_str}}}")
#     else:
#         result.append(f"{indent_str}+ {key}: {d2[key]}")
#
#     return result
#
#
# def compare_files_stylish(file1, file2, indent=4):
#     with open(file1) as f1, open(file2) as f2:
#         j_file1 = json.load(f1)
#         j_file2 = json.load(f2)
#
#     result = compare_dicts(j_file1, j_file2, 0, indent)
#     return '\n'.join(result)

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


def handle_both_keys(d1, d2, key, indent_level, indent):
    result = []
    indent_str = ' ' * (indent * indent_level)

    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        result.append(f"{indent_str}{key}: {{")
        result.extend(compare_dicts(d1[key], d2[key], indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    elif d1[key] != d2[key]:
        result.append(f"{indent_str}- {key}: {d1[key]}")
        result.append(f"{indent_str}+ {key}: {d2[key]}")
    else:
        result.append(f"{indent_str}  {key}: {d1[key]}")

    return result


def handle_key_in_d1(d1, key, indent_level, indent):
    result = []
    indent_str = ' ' * (indent * indent_level)

    if isinstance(d1[key], dict):
        result.append(f"{indent_str}- {key}: {{")
        result.extend(compare_dicts(d1[key], {}, indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    else:
        result.append(f"{indent_str}- {key}: {d1[key]}")

    return result


def handle_key_in_d2(d2, key, indent_level, indent):
    result = []
    indent_str = ' ' * (indent * indent_level)

    if isinstance(d2[key], dict):
        result.append(f"{indent_str}+ {key}: {{")
        result.extend(compare_dicts({}, d2[key], indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    else:
        result.append(f"{indent_str}+ {key}: {d2[key]}")

    return result


def compare_files_stylish(file1, file2, indent=4):
    data1 = load_data(file1)
    data2 = load_data(file2)

    result = compare_dicts(data1, data2, 0, indent)
    return '\n'.join(result)
