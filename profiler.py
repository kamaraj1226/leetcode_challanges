import argparse
import shutil
import os
import subprocess


def clean_destination():
    file = "profiler/do_profile.py"

    if os.path.exists(file):
        os.remove(file)


def main(file, parent_dir):
    _source = parent_dir + "/" + file

    new_file_name = "do_profile.py"
    _dest = "profiler/" + new_file_name
    clean_destination()
    shutil.copy2(_source, _dest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--name", help="Python file to do profiling", required=True
    )
    parser.add_argument(
        "-p", "--parent_dir", default="non-completed", help="Parent directory"
    )

    args = parser.parse_args()
    main(args.name, args.parent_dir)
