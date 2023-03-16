import json


def load_json_file(file_path):
    with open(file_path) as f:
        return json.load(f)


def compare_values(val1, val2, path):
    if val1 == val2:
        return []
    if isinstance(val1, dict) and isinstance(val2, dict):
        return compare_dicts(val1, val2, path)
    if isinstance(val1, dict):
        return [f"Property '{path}' was updated. "
                f"From [complex value] to {val2}"]
    return [f"Property '{path}' was updated. "
            f"From {val1} to {val2}"]


def compare_dicts(d1, d2, path=''):
    result = []
    keys = sorted(set(d1.keys()).union(d2.keys()))
    for key in keys:
        p = f"{path}.{key}" if path else key
        if key in d1 and key in d2:
            result.extend(compare_values(d1[key], d2[key], p))
        elif key in d1:
            result.append(f"Property '{p}' was removed")
        elif key in d2:
            value = d2[key]
            if isinstance(value, dict):
                result.append(f"Property '{p}' was added with value: "
                              f"[complex value]")
            else:
                result.append(f"Property '{p}' was added with value: {value}")
    return result


def compare_files_plain(file_path1, file_path2):
    j_file1 = load_json_file(file_path1)
    j_file2 = load_json_file(file_path2)
    result = compare_dicts(j_file1, j_file2)
    return '\n'.join(result)