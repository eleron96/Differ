import argparse
import gendiff.scripts.diff_json as diff_json
import os


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='First file to compare')
    parser.add_argument('second_file', help='Second file to compare')
    parser.add_argument('-f', '--format', dest='format', default='pretty', help='set format of output')

    args = parser.parse_args()
    first_file_path = os.path.join('gendiff', args.first_file)
    second_file_path = os.path.join('gendiff', args.second_file)
    print(diff_json.compare_files(first_file_path, second_file_path))


if __name__ == '__main__':
    main()
