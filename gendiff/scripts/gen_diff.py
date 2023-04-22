from ..generate_differ import generate_diff
from ..parse_args import parse_args


def main():
    args = parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
