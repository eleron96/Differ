import json


def load_json_file(file_path):
    with open(file_path) as f:
        return json.load(f)


def compare_dicts(d1, d2, path=''):
    result = []
    keys = sorted(set(d1.keys()).union(d2.keys()))
    for key in keys:
        p = f"{path}.{key}" if path else key
        if key in d1 and key in d2:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                result.extend(compare_dicts(d1[key], d2[key], path=p))
            elif d1[key] != d2[key]:
                if isinstance(d1[key], dict):
                    result.append(f"Property '{p}' was updated. "
                                  f"From [complex value] to {d2[key]}")
                else:
                    result.append(f"Property '{p}' was updated. "
                                  f"From {d1[key]} to {d2[key]}")
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
