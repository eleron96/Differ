# import argparse
# import gendiff.scripts.diff_stylish as diff_stylish
# import gendiff.scripts.diff_plain as diff_plain
# import gendiff.scripts.diff_json as diff_json
# import os
#
#
# def parse_arguments():
#     parser = argparse.ArgumentParser(
#         description='Compares two configuration files and shows a difference.'
#     )
#     parser.add_argument('first_file', help='First file to compare')
#     parser.add_argument('second_file', help='Second file to compare')
#     parser.add_argument('-f', '--format', dest='format',
#                         default='stylish', help='set format of output')
#
#     return parser.parse_args()
#
#
# def generate_diff(first_file, second_file, format):
#     first_file_path = os.path.join('gendiff', first_file)
#     second_file_path = os.path.join('gendiff', second_file)
#
#     if format == "stylish":
#         return diff_stylish.compare_files_stylish(first_file_path, second_file_path)
#     elif format == "plain":
#         return diff_plain.compare_files_plain(first_file_path, second_file_path)
#     elif format == "json":
#         return diff_json.compare_files_json(first_file_path, second_file_path)
#
#
# if __name__ == "__main__":
#     args = parse_arguments()
#     result = generate_diff(args.first_file, args.second_file, args.format)
#     print(result)


import argparse
import gendiff.scripts.diff_stylish as diff_stylish
import gendiff.scripts.diff_plain as diff_plain
import gendiff.scripts.diff_json as diff_json
import os


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file to compare')
    parser.add_argument('second_file', help='Second file to compare')
    parser.add_argument('-f', '--format', dest='format',
                        default='stylish', help='set format of output')

    return parser.parse_args()


def generate_diff(first_file, second_file, format='stylish'):
    first_file_path = os.path.abspath(first_file)
    second_file_path = os.path.abspath(second_file)

    if format == "stylish":
        return diff_stylish.compare_files_stylish(first_file_path, second_file_path)
    elif format == "plain":
        return diff_plain.compare_files_plain(first_file_path, second_file_path)
    elif format == "json":
        return diff_json.compare_files_json(first_file_path, second_file_path)


if __name__ == "__main__":
    args = parse_arguments()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)
