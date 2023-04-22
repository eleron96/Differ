import pytest
from gendiff.generate_differ import generate_diff
from gendiff.parse_args import parse_args


def test_parse_args_basic():
    args = ['file1', 'file2']
    parsed_args = parse_args(args)

    assert parsed_args.first_file == 'file1'
    assert parsed_args.second_file == 'file2'
    assert parsed_args.format == 'stylish'


def test_parse_args_with_format():
    args = ['file1', 'file2', '-f', 'plain']
    parsed_args = parse_args(args)

    assert parsed_args.first_file == 'file1'
    assert parsed_args.second_file == 'file2'
    assert parsed_args.format == 'plain'


def test_parse_args_with_long_format():
    args = ['file1', 'file2', '--format', 'json']
    parsed_args = parse_args(args)

    assert parsed_args.first_file == 'file1'
    assert parsed_args.second_file == 'file2'
    assert parsed_args.format == 'json'


@pytest.mark.parametrize(
    "args,expected_first_file,expected_second_file,expected_format",
    [
        (['file1', 'file2'], 'file1', 'file2', 'stylish'),
        (['file1', 'file2', '-f', 'plain'], 'file1', 'file2', 'plain'),
        (['file1', 'file2', '--format', 'json'], 'file1', 'file2', 'json'),
    ],
)
def test_parse_args_parametrized(args, expected_first_file,
                                 expected_second_file, expected_format):
    parsed_args = parse_args(args)

    assert parsed_args.first_file == expected_first_file
    assert parsed_args.second_file == expected_second_file
    assert parsed_args.format == expected_format
