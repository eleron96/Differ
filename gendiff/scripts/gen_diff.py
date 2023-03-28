# import argparse
# import gendiff.scripts.diff_stylish as diff_stylish
# import gendiff.scripts.diff_plain as diff_plain
# import gendiff.scripts.diff_json as diff_json
# import os
#
#
# def generate_diff():
#     parser = argparse.ArgumentParser(
#         prog='gendiff',
#         description='Compares two configuration files and shows a difference.'
#     )
#     parser.add_argument('first_file', help='First file to compare')
#     parser.add_argument('second_file', help='Second file to compare')
#     parser.add_argument('-f', '--format', dest='format',
#                         default='stylish', help='set format of output')
#
#     args = parser.parse_args()
#     first_file_path = os.path.join('gendiff', args.first_file)
#     second_file_path = os.path.join('gendiff', args.second_file)
#
#     if args.format == "stylish":
#         print(diff_stylish.compare_files_stylish(first_file_path,
#                                                  second_file_path))
#     elif args.format == "plain":
#         print(diff_plain.compare_files_plain(first_file_path, second_file_path))
#     elif args.format == "json":
#         print(diff_json.compare_files_json(first_file_path, second_file_path))
#
#
# if __name__ == '__main__':
#     generate_diff()


from gendiff.scripts import diff_stylish, diff_plain, diff_json
import argparse
import os

def generate_diff(file_path1, file_path2, format_name='stylish'):
    first_file_path = os.path.join('gendiff', file_path1)
    second_file_path = os.path.join('gendiff', file_path2)

    if format_name == "stylish":
        return diff_stylish.compare_files_stylish(first_file_path, second_file_path)
    elif format_name == "plain":
        return diff_plain.compare_files_plain(first_file_path, second_file_path)
    elif format_name == "json":
        return diff_json.compare_files_json(first_file_path, second_file_path)

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file to compare')
    parser.add_argument('second_file', help='Second file to compare')
    parser.add_argument('-f', '--format', dest='format',
                        default='stylish', help='set format of output')

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()


