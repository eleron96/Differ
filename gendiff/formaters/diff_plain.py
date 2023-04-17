def stringify(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif value is None:
        return 'null'
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def render(tree, path_key=""):
    result = []

    if 'key' in tree:
        path_key = f"{path_key}.{tree['key']}" if path_key else tree['key']

    children = tree.get('children', [])
    for child in children:
        result += render(child, path_key)

    node_type = tree['type']
    if node_type == 'added':
        value = stringify(tree['value'])
        if value == '[complex value]':
            result.append(f"Property '{path_key}' was added with value: {value}")
        else:
            result.append(f"Property '{path_key}' was added with value: {value}")
    elif node_type == 'removed':
        result.append(f"Property '{path_key}' was removed")
    elif node_type == 'changed':
        value_1 = stringify(tree['value_1'])
        value_2 = stringify(tree['value_2'])
        if value_1 == '[complex value]':
            result.append(f"Property '{path_key}' was updated. From {value_1} to {value_2}")
        else:
            result.append(f"Property '{path_key}' was updated. From {value_1} to {value_2}")
    elif node_type == 'no_changes':
        pass
    return result
