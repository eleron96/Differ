import json


def handle_both_keys(indent_str, key, d1, d2, indent_level, indent):
    result = []
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


def handle_single_key(indent_str, key, d, is_add, indent_level, indent):
    result = []
    symbol = "+" if is_add else "-"
    if isinstance(d[key], dict):
        result.append(f"{indent_str}{symbol} {key}: {{")
        result.extend(compare_dicts(d[key], {}, indent_level + 1, indent) if is_add else compare_dicts({}, d[key], indent_level + 1, indent))
        result.append(f"{indent_str}}}")
    else:
        result.append(f"{indent_str}{symbol} {key}: {d[key]}")
    return result


def compare_dicts(d1, d2, indent_level, indent):
    indent_str = ' ' * (indent * indent_level)
    result = []
    keys = sorted(set(d1.keys()).union(d2.keys()))
    for key in keys:
        if key in d1 and key in d2:
            result.extend(handle_both_keys(indent_str, key, d1, d2, indent_level, indent))
        elif key in d1:
            result.extend(handle_single_key(indent_str, key, d1, False, indent_level, indent))
        elif key in d2:
            result.extend(handle_single_key(indent_str, key, d2, True, indent_level, indent))
    return result


def compare_files_json(file1, file2, indent=4):
    with open(file1) as f1, open(file2) as f2:
        j_file1 = json.load(f1)
        j_file2 = json.load(f2)
    result = compare_dicts(j_file1, j_file2, 0, indent)
    return '\n'.join(result)
