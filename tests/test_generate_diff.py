import pytest
import json
from faker import Faker
from gendiff import generate_diff

faker = Faker()


def create_random_data():
    return {
        "key1": faker.word(),
        "key2": faker.word(),
        "key3": {
            "key3_1": faker.word(),
            "key3_2": faker.word()
        }
    }


def test_generate_diff_stylish_format_with_random_data():
    data1 = create_random_data()
    data2 = create_random_data()

    file_path1 = 'file1.json'
    file_path2 = 'file2.json'

    with open(file_path1, 'w') as f:
        json.dump(data1, f)

    with open(file_path2, 'w') as f:
        json.dump(data2, f)

    output = generate_diff(file_path1, file_path2, format_name='stylish')
    assert isinstance(output, str)


def test_generate_diff_plain_format_with_random_data():
    data1 = create_random_data()
    data2 = create_random_data()

    file_path1 = 'file1.json'
    file_path2 = 'file2.json'

    with open(file_path1, 'w') as f:
        json.dump(data1, f)

    with open(file_path2, 'w') as f:
        json.dump(data2, f)

    output = generate_diff(file_path1, file_path2, format_name='plain')
    assert isinstance(output, str)


def test_generate_diff_json_format_with_random_data():
    data1 = create_random_data()
    data2 = create_random_data()

    file_path1 = 'file1.json'
    file_path2 = 'file2.json'

    with open(file_path1, 'w') as f:
        json.dump(data1, f)

    with open(file_path2, 'w') as f:
        json.dump(data2, f)

    output = generate_diff(file_path1, file_path2, format_name='json')
    assert isinstance(output, str)
