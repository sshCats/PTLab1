# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JsonDataReader import JsonDataReader
from StudentSelection import StudentSelection


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if path.endswith('.txt'):
        reader = TextDataReader()
    elif path.endswith('.json'):
        reader = JsonDataReader()
    else:
        raise ValueError('Error: wrong file extension')

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    print("Sorted rating: ",
          dict(sorted(rating.items(), key=lambda kv: kv[1])))

    selection = StudentSelection(rating).select()
    print("Third quartile selection: ", selection)


if __name__ == "__main__":
    main()
