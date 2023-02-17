import json

# j_file1 = json.load(open('file1.json'))
# j_file2 = json.load(open('file2.json'))


def compare_files(file1, file2):
    j_file1 = json.load(open(file1))
    j_file2 = json.load(open(file2))
    keys = sorted(set(j_file1.keys()).union(j_file2.keys()))
    return [compare_key_values(key, j_file1, j_file2) for key in keys]

def compare_key_values(key, j_file1, j_file2):
    if key not in j_file1:
        return f"+ {key}: {j_file2[key]}"
    elif key not in j_file2:
        return f"- {key}: {j_file1[key]}"
    elif j_file1[key] == j_file2[key]:
        return f"  {key}: {j_file1[key]}"
    else:
        return f"- {key}: {j_file1[key]}\n+ {key}: {j_file2[key]}"

# def compare_files(file1, file2):
#     j_file1 = json.load(open(file1))
#     j_file2 = json.load(open(file2))
#     keys = sorted(set(j_file1.keys()).union(j_file2.keys()))
#     for key in keys:
#         if key in j_file1 and key in j_file2:
#             if j_file1[key] != j_file2[key]:
#                 print(f"- {key}: {j_file1[key]}")
#                 print(f"+ {key}: {j_file2[key]}")
#             else:
#                 print(f"  {key}: {j_file1[key]}")
#         elif key in j_file1:
#             print(f"- {key}: {j_file1[key]}")
#         elif key in j_file2:
#             print(f"+ {key}: {j_file2[key]}")


# compare_files(j_file1, j_file2)
