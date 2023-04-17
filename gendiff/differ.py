def node_processing(data1, data2):
    childrens = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key not in data2:  # key not in second file
            childrens.append({
                'type': 'removed',
                'key': key,
                'value': data1[key]
            })
        elif key not in data1:  # key added
            childrens.append({
                'type': 'added',
                'key': key,
                'value': data2[key]
            })
        elif isinstance(data2[key], dict) and isinstance(data1[key], dict):
            childrens.append({
                'type': 'nest',
                'key': key,
                'children': node_processing(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            childrens.append({
                'type': 'changed',
                'key': key,
                'value_1': data1[key],
                'value_2': data2[key]
            })
        else:
            childrens.append({
                'type': 'no_changes',
                'key': key,
                'value': data2[key]
            })
    return childrens


def build(data1, data2):
    return {
        'type': 'differ',
        'children': node_processing(data1, data2)
    }
