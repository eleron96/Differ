import os
import json
import tempfile
import gendiff.scripts.diff_json as diff_json
import gendiff.scripts.diff_plain as diff_plain
import gendiff.scripts.diff_stylish as diff_stylish
from gendiff.scripts import gen_diff as gn
import pytest



def test_compare_files():
    # create two temporary .json files
    file1 = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    file2 = tempfile.NamedTemporaryFile(delete=False, suffix='.json')

    # write sample data to the files
    sample_data = {'key1': 'value1', 'key2': 'value2'}
    with open("file1.json", "w") as file1:
        json.dump(sample_data, file1)
    with open("file2.json", "w") as file2:
        json.dump({'key1': 'value1', 'key2': 'value3'}, file2)

    # call the compare_files function with the two files
    diff_json.compare_files_json(file1.name, file2.name)
    diff_plain.compare_files_plain(file1.name, file2.name)
    diff_stylish.compare_files_stylish(file1.name, file2.name)
    os.unlink(file1.name)
    os.unlink(file2.name)


def test_main_no_args(capsys):
    with pytest.raises(SystemExit):
        gn.generate_diff()
    captured = capsys.readouterr()
    assert captured.err.startswith("usage: gendiff")
    assert captured.out == ""



