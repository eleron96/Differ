def build_ident(depth, marker=' '):
    return ' ' * (depth * 4 - 2) + f"{marker} "


def stringify(value, depth=1):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return "true" if value else "false"
    if not isinstance(value, dict):
        return str(value)
    lines = []
    ident = build_ident(depth + 1)
    for key in value:
        formatted_value = stringify(value[key], depth + 1)
        lines.append(f'{ident}{key}: {formatted_value}')
    result = '\n'.join(lines)
    return f'{{\n{result}\n{build_ident(depth)}}}'


def render(tree, depth=0):  # noqa: C901
    children = tree.get('children')
    value = stringify(tree.get('value'), depth=depth)
    value_1 = stringify(tree.get('value_1'), depth=depth)
    value_2 = stringify(tree.get('value_2'), depth=depth)
    node_type = tree['type']
    ident = build_ident(depth)
    ident_minus = build_ident(depth, marker='-')
    ident_plus = build_ident(depth, marker='+')

    if node_type == 'differ':
        lines = map(lambda node: render(node, depth + 1), children)
        result = "\n".join(lines)

        return f'{{\n{result}\n}}'
    elif node_type == "nest":
        lines = map(lambda node: render(node, depth + 1), children)
        result = "\n".join(lines)
        return f'{ident}{tree["key"]}: {{\n{result}\n{ident}}}'

    elif node_type == "removed":
        return f'{ident_minus}{tree["key"]}: {value}'

    elif node_type == "added":
        return f'{ident_plus}{tree["key"]}: {value}'

    elif node_type == "changed":
        lines = [
            f'{ident_minus}{tree["key"]}: {value_1}',
            f'{ident_plus}{tree["key"]}: {value_2}'
        ]
        return '\n'.join(lines)
    elif node_type == "no_changes":
        return f'{ident}{tree["key"]}: {value}'

    raise ValueError(f'Unknown node type: {node_type}')
