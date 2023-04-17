import json


def render(tree):
    return json.dumps(tree, indent=2)
