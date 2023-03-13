import json


def compare_files_json(file1, file2):
    j_file1 = json.load(open(file1))
    j_file2 = json.load(open(file2))

    def compare_values(value1, value2):
        if isinstance(value1, dict) and isinstance(value2, dict):
            return compare_dicts(value1, value2)
        elif value1 != value2:
            return {
                "type": "updated",
                "old_value": value1,
                "new_value": value2
            }

    def compare_dicts(d1, d2, path=''):
        result = []
        keys = sorted(set(d1.keys()).union(d2.keys()))
        for key in keys:
            p = f"{path}.{key}" if path else key
            if key in d1 and key in d2:
                comparison_result = compare_values(d1[key], d2[key])
                if comparison_result is not None:
                    if isinstance(comparison_result, list):
                        result.extend(comparison_result)
                    else:
                        comparison_result["property"] = p
                        result.append(comparison_result)
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
                        "value": compare_dicts({}, value)
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
