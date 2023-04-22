from gendiff import differ
from gendiff.formaters import diff_stylish, diff_plain, diff_json
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


def generate_diff(file_path1, file_path2, format_name='stylish'):
    d1 = load_data(file_path1)
    d2 = load_data(file_path2)
    tree = differ.build(d1, d2)

    if format_name == "stylish":
        return diff_stylish.render(tree)
    elif format_name == "plain":
        output = diff_plain.render(tree)
        return '\n'.join(output)
    elif format_name == "json":
        return diff_json.render(tree)
