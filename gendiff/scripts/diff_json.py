import json


# j_file1 = json.load(open('file1.json'))
# j_file2 = json.load(open('file2.json'))

def compare_files(file1, file2, indent=4):
    j_file1 = json.load(open(file1))
    j_file2 = json.load(open(file2))

    def compare_dicts(d1, d2, indent_level):
        indent_str = ' ' * (indent * indent_level)
        result = []
        keys = sorted(set(d1.keys()).union(d2.keys()))
        for key in keys:
            if key in d1 and key in d2:
                if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    result.append(f"{indent_str}{key}: {{")
                    result.extend(compare_dicts(d1[key],
                                                d2[key], indent_level + 1))
                    result.append(f"{indent_str}}}")
                elif d1[key] != d2[key]:
                    result.append(f"{indent_str}- {key}: {d1[key]}")
                    result.append(f"{indent_str}+ {key}: {d2[key]}")
                else:
                    result.append(f"{indent_str}  {key}: {d1[key]}")
            elif key in d1:
                if isinstance(d1[key], dict):
                    result.append(f"{indent_str}- {key}: {{")
                    result.extend(compare_dicts(d1[key], {}, indent_level + 1))
                    result.append(f"{indent_str}}}")
                else:
                    result.append(f"{indent_str}- {key}: {d1[key]}")
            elif key in d2:
                if isinstance(d2[key], dict):
                    result.append(f"{indent_str}+ {key}: {{")
                    result.extend(compare_dicts({}, d2[key], indent_level + 1))
                    result.append(f"{indent_str}}}")
                else:
                    result.append(f"{indent_str}+ {key}: {d2[key]}")
        return result

    result = compare_dicts(j_file1, j_file2, 0)
    return '\n'.join(result)


def compare_files_plain(file1, file2):
    j_file1 = json.load(open(file1))
    j_file2 = json.load(open(file2))

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
                        result.append(f"Property '{p}' was updated."
                                      f" From [complex value] to {d2[key]}")
                    else:
                        result.append(f"Property '{p}' was updated."
                                      f" From {d1[key]} to {d2[key]}")
            elif key in d1:
                result.append(f"Property '{p}' was removed")
            elif key in d2:
                value = d2[key]
                if isinstance(value, dict):
                    result.append(f"Property '{p}' "
                                  f"was added with value: [complex value]")
                else:
                    result.append(f"Property '{p}' "
                                  f"was added with value: {value}")
        return result

    result = compare_dicts(j_file1, j_file2)
    return '\n'.join(result)


def compare_files_json(file1, file2):
    j_file1 = json.load(open(file1))
    j_file2 = json.load(open(file2))

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
                        result.append({
                            "type": "updated",
                            "property": p,
                            "old_value": "[complex value]",
                            "new_value": d2[key]
                        })
                    else:
                        result.append({
                            "type": "updated",
                            "property": p,
                            "old_value": d1[key],
                            "new_value": d2[key]
                        })
            elif key in d1:
                result.append({
                    "type": "removed",
                    "property": p
                })
            elif key in d2:
                value = d2[key]
                if isinstance(value, dict):
                    result.append({
                        "type": "added",
                        "property": p,
                        "value": "[complex value]"
                    })
                else:
                    result.append({
                        "type": "added",
                        "property": p,
                        "value": value
                    })
        return result

    result = compare_dicts(j_file1, j_file2)
    return json.dumps(result, indent=4)

# compare_files(j_file1, j_file2)
