import json


# flake8: noqa: C901
def compare_dicts(d1, d2, indent_level, indent):
    indent_str = ' ' * (indent * indent_level)
    result = []
    keys = sorted(set(d1.keys()).union(d2.keys()))
    for key in keys:
        if key in d1 and key in d2:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                result.append(f"{indent_str}{key}: {{")
                result.extend(compare_dicts(d1[key],
                                            d2[key], indent_level + 1, indent))
                result.append(f"{indent_str}}}")
            elif d1[key] != d2[key]:
                result.append(f"{indent_str}- {key}: {d1[key]}")
                result.append(f"{indent_str}+ {key}: {d2[key]}")
            else:
                result.append(f"{indent_str}  {key}: {d1[key]}")
        elif key in d1:
            if isinstance(d1[key], dict):
                result.append(f"{indent_str}- {key}: {{")
                result.extend(compare_dicts(d1[key],
                                            {}, indent_level + 1, indent))
                result.append(f"{indent_str}}}")
            else:
                result.append(f"{indent_str}- {key}: {d1[key]}")
        elif key in d2:
            if isinstance(d2[key], dict):
                result.append(f"{indent_str}+ {key}: {{")
                result.extend(compare_dicts({},
                                            d2[key], indent_level + 1, indent))
                result.append(f"{indent_str}}}")
            else:
                result.append(f"{indent_str}+ {key}: {d2[key]}")
    return result


def compare_files_json(file1, file2, indent=4):
    j_file1 = json.load(open(file1))
    j_file2 = json.load(open(file2))
    result = compare_dicts(j_file1, j_file2, 0, indent)
    return '\n'.join(result)
