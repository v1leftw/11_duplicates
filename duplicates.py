import os
import argparse
from collections import namedtuple, defaultdict


def get_args():
    parser = argparse.ArgumentParser(description="Enter the path:")
    parser.add_argument("-path", required=True, help="Path to file")
    return parser.parse_args()


def get_all_files(directory_path):
    # based on https://stackoverflow.com/a/40061513/8482475
    dict_of_files = defaultdict(list)
    file_description = namedtuple("File", "Name Size")
    for root, dirs, files in os.walk(directory_path, topdown=True):
        for name in files:
            path_to_file = os.path.join(root, name)
            description = file_description(name, os.path.getsize(path_to_file))
            # Creates dictionary where key stores description of the file
            # and value stores all paths to this file
            dict_of_files[description].append(path_to_file)
    return dict_of_files


def find_duplicates(file_list):
    return {description: paths for (description, paths) in file_list.items()
            if len(paths) > 1}


if __name__ == "__main__":
    path = get_args().path
    duplicates = find_duplicates(get_all_files(path))
    for file, file_paths in duplicates.items():
        print("File: {}. Size: {}. Copies at: ".format(file.Name, file.Size))
        for path in file_paths:
            print("- ", path)
        print("\t")  # file-divider
