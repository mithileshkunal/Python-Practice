import sys
import os
from datetime import datetime


def file_read(file_name):
    try:
        f = open(file_name, "r")
        print(f.readline())
    except FileNotFoundError:
        print(sys.exc_info()[1])
    else:
        f.close()


def file_write(file_name):
    f = open(file_name, "w")
    f.write(f"{datetime.now()} Hello World\n")
    f.close()


def file_append(file_name):
    f = open(file_name, "a")
    f.write(f"{datetime.now()} New line is appended\n")
    f.close()


def delete_file_if_present(file_path):
    f = os.path.isfile(file_path)
    if f:
        os.remove(file_path)


def file_read_context_mgr(file_path):
    with open(file_path, "r") as f:
        for line in f.readlines():
            print(line, end="")


def file_append_ctx_mgr(file_path):
    with open(file_path, "a") as f:
        f.write(f"{datetime.now()}: This line is appended\n")


def print_file_content(file_name):
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")


def copy_file_content(inp_file, out_file):
    with open(inp_file, "rb") as sf:
        with open(out_file, "wb") as df:
            for line in sf:
                df.write(line)


if __name__ == "__main__":
    # delete_file_if_present("sample.txt")
    # file_write("sample.txt")
    # file_append("sample.txt")
    # file_read("sample.txt")
    # file_append_ctx_mgr("sample.txt")
    # file_read_context_mgr("sample.txt")
    copy_file_content("inp.png", "out.png")
    # print_file_content("sample.txt")
