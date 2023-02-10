import json

j_file1 = json.load(open('scripts/file1.json'))
j_file2 = json.load(open('scripts/file2.json'))

def compare_files(file1, file2):
    keys = sorted(set(file1.keys()).union(file2.keys()))
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] != file2[key]:
                print(f"- {key}: {file1[key]}")
                print(f"+ {key}: {file2[key]}")
            else:
                print(f"  {key}: {file1[key]}")
        elif key in file1:
            print(f"- {key}: {file1[key]}")
        elif key in file2:
            print(f"+ {key}: {file2[key]}")


compare_files(j_file1, j_file2)

