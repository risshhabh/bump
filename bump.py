#!/usr/bin/env python3

"""
bump - Better coMPile
"""

import os
from sys import argv

# Edit to change compile command
cmd = "g++-12 -std=c++17 -pedantic-errors -Wall -Wextra -Weffc++ -Wsign-conversion -Werror -fmax-errors=1 -o "


def print_help_page() -> int:
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
        + " bump OR bump -h OR bump --help             "
        + comment("# Help page")
    )

    print(final_output)

    return 0


if len(argv) == 1:
    print_help_page()
