import json
import gendiff.scripts.diff_json as diff_json

def test_compare_files():
    file1 = 'gendiff/file1.json'
    file2 = 'gendiff/file2.json'

    # create test data
    data = {'key1': 'value1', 'key2': 'value2'}
    with open(file1, 'w') as f:
        json.dump(data, f)

    data = {'key1': 'value1', 'key3': 'value3'}
    with open(file2, 'w') as f:
        json.dump(data, f)

    # run the compare_files function
    result = diff_json.compare_files(file1, file2)

    # assert the result
    expected_result = '''- key2: value2
+ key3: value3
  key1: value1
'''
    assert result == expected_result

    # cleanup the test data
    import os
    os.remove(file1)
    os.remove(file2)

