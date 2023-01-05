#!/usr/bin/env python3

"""
bump - Better coMPile
"""

import os
from sys import argv
from sys import exit as sys_exit

# Edit to change compile command
cmd = "g++-12 -std=c++17 -pedantic-errors -Wall -Wextra -Weffc++ -Wsign-conversion -Werror -fmax-errors=1 -o "  # `-o ` at end is required


def print_help_page() -> int:
    """
    Painfully print out help page
    """
    from termcolor import colored

    bold = lambda text: colored(text, attrs=["bold"])
    comment = lambda text: colored(text, "green")
    purple = lambda text: colored(text, "magenta")
    prompt = colored("$", "grey")

    final_output = (
        bold("Commands:\n")
        + prompt
        + " bump -c "
        + purple("$FILE")
        + "   OR bump --compile "
        + purple("$FILE")
        + comment("    # Compile `file` if it is in ./src/\n")
        + prompt
        + " bump -a         OR bump --all              "
        + comment("# Compile every file in ./src/ to ./target/\n")
        + prompt
        + " bump -xa        OR bump --clearall         "
        + comment("# Delete every executable in ./target/\n")
        + prompt
        + " bump -x "
        + purple("$FILE")
        + "   OR bump --clear "
        + purple("$FILE")
        + comment("      # Delete `file` if it is an executable in ./target/\n")
        + prompt
        + " bump -h OR bump OR bump --help             "
        + comment("# Help page")
    )

    print(final_output)

    return 0


argslen = len(argv) - 1

if argslen == 0:  # `bump` -> help page
    print_help_page()
    sys_exit()

if argslen > 2:
    print(
        "You have entered more than two arguments. If your filename has spaces in it, enclose it in quotes and rerun the command."
    )
    sys_exit()


cpp_files = []


def cpp_list() -> int:
    """
    Get list of C++ files in `./src`.
    """

    # First check if ./src exists
    if "src" not in os.listdir():
        print("`src/` does not exist")
        return 0

    global cpp_files

    # First, get relative path of every C++ file
    for root, dirs, files in os.walk("./src"):
        for file in files:
            if (
                os.path.splitext(file)[-1].lower() in (".cpp", ".cc", ".cxx")
                or os.path.splitext(file)[-1] == ".C"
            ):
                cpp_files.append(os.path.join(root, file))

    return 1


def clear_target() -> int:
    """
    Delete entire ./target folder
    """

    # First check if there is ./target
    if "target" not in os.listdir():
        print("`target/` does not exist")
        return 0

    check = input("Really clear `target/`? (Y/N) ")
    if check.lower() in ("y", "yes"):
        os.system("rm -rf ./target")
        # * https://github.com/nivekuil/rip
        # os.system("rip ./target")

        print("Cleared ./target")
        return 0
    elif check.lower() in ("n", "no"):
        print("Cancelled clear")
        return 0
    else:
        print("Invalid input")
        return 0


def check_cpp(cpp_file: str) -> int:
    """
    Check if inputted file exists in ./src and is a C++ file.
    """

    # First check if `src/ exists`
    if "src" not in os.listdir():
        print("`src/` does not exist")
        return 0

    global cpp_files

    from pathlib import Path

    if Path(cpp_file).is_file() and (  # Check if file
        os.path.splitext(cpp_file)[-1].lower()
        in (".cpp", ".cc", ".cxx")  # Check if file is C++
    ):
        cpp_files.append(cpp_file)
        return 1
    else:
        print(
            """File either does not exist or is not a C++ file
        Check its path and extension"""
        )
        return 0


def del_file(exec_file):
    """
    Check if inputted file is an executable in ./target then delete it
    """

    # First check if `target/` exists
    if "target" not in os.listdir():
        print("`target/` does not exist")

    from pathlib import Path

    if not Path(exec_file).is_file():  # File exists check
        print(f"Cannot locate file {Path(exec_file)}")
        return 0
    elif not len(os.path.splitext(exec_file)[-1]) == 0:  # File extension check
        print(
            "File is either not an executable or has a file extension and will not be deleted"
        )
        return 0
    elif os.access(exec_file, os.X_OK):  # File executable permissions check
        print("File is not an executable and will not be deleted")
        return 0


if argslen == 1:
    flags = {
        "-a": cpp_list,
        "-xa": clear_target,
        "-h": print_help_page,
        "--all": cpp_list,
        "--clearall": clear_target,
        "--help": print_help_page,
    }

    if argv[1] in flags:
        out = flags[argv[1]]()
        if out == 0:  # 0 = exit, 1 = continue
            sys_exit()

elif argslen == 2:
    flags = {
        "-c": check_cpp,
        "-x": del_file,
        "--compile": check_cpp,
        "--clear": del_file,
    }

    if argv[1] in flags:
        out = flags[argv[1]](argv[2])
        if out == 0:  # 0 = exit, 1 = continue
            sys_exit()


# If program has not been exited, then the files must be compiled,
# But if there are no files in `cpp_files` that need to be compiled,
# Then the command run is invalid; exit program with error.
if len(cpp_files) == 0:
    print("Invalid command")
    sys_exit()

# Go ahead and compile all files
for src_path in cpp_files:

    # Get executable file path for each `src_path`
    target_path = os.path.splitext(src_path.replace(src_path[0:5], "./target", 1))[0]

    # First, ensure the enclosing folder of the executable path exists.
    try:
        os.makedirs(os.path.dirname(os.path.abspath(target_path)))
    except FileExistsError:
        pass

    os.system(f"{cmd} {target_path} {src_path}")

print(f"Compiled {len(cpp_files)} files")


"""
TODO
- `bump init project/path/` to initialize a project
"""
