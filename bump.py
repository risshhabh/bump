#!/usr/bin/env python3

"""
bump - Better coMPile
"""

import os
from sys import argv
from sys import exit as sys_exit

# Edit to change compile command
cmd = "g++-12 -std=c++17 -pedantic-errors -Wall -Wextra -Weffc++ -Wsign-conversion -Werror -fmax-errors=1 -o "  # `-o ' at end is required


def print_help_page() -> str:
    """
    PainfulPrint out help page
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

    return "ed with pain"


argslen = len(argv) - 1

if argslen == 0:  # `bump' -> help page
    print_help_page()
    sys_exit()

if argslen > 2:
    print(
        "You have entered more than two arguments. if your filename has spaces in it, enclose it in quotes and rerun the command."
    )
    sys_exit()


cpp_files = []


def cpp_list() -> int:
    """
    Get list of C++ files in `./src'.
    """
    global cpp_files

    # First, get relative path of every C++ file
    for root, dirs, files in os.walk("./src"):
        for file in files:
            if file.endswith((".cpp", ".cc", ".cxx")):
                cpp_files.append(os.path.join(root, file))

    return 1


def clear_target() -> int:
    """
    Delete entire ./target folder
    """
    check = input("Really clear `./target'? (Y/N) ")
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


def check_cpp() -> None:
    pass


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
        "-c": "check_cpp",  # TODO
        "-x": "clear_file",
        "--compile": "check_cpp",
        "--clear": "clear_file",
    }

    if argv[1] in flags:
        out = flags[argv[1]](argv[2])
        if out == 0:  # 0 = exit, 1 = continue
            sys_exit()


# If program has not been exited, then the command is invalid
