Progress program to my final version at [risshhabh/wish](https://github.com/risshhabh/wish).

# bump - Better coMPile

An easier C++ compile command.

`bump` assumes the following project file structure for a program:
```
.
├── src/
│   └── C++ files and subfolders
└── target/
    └── executables in corresponding folders
```
Which is mostly similar to [Rust's](https://www.rust-lang.org/) file structure.

##### *I do not recommend you to use bump if you are on Windows; Makefile and other methods are better. I use bump because it is easiest for me.*

## How to use (zsh on Mac)
1. Ensure you have [Python3](https://www.python.org/downloads/) installed by running
```console
$ python3 --version
```
which should output `Python 3.version`. If you do not have Python3 installed, install it at [python.org](https://www.python.org/downloads/).

2. After installing Python3, download the `bump.py` file.
3. Give `bump.py` executable permissions by running `chmod +x path/to/bump.py`
4. Go to your `~/.zshrc` and add `bump="/path/to/bump.py"` to it.
5. Either reload/exit your terminal or type `source ~/.zshrc` to apply the updated configurations for `.zshrc`.

## Commands
```console
$ bump -c $FILE   OR bump --compile $FILE    # Compile `file` if it is in ./src/
$ bump -a         OR bump --all              # Compile every file in ./src/ to ./target/
$ bump -xa        OR bump --clearall         # Delete every executable in ./target/
$ bump -x $FILE   OR bump --clear $FILE      # Delete `file` if it is an executable in ./target/
$ bump -h OR bump OR bump --help             # Help page
```

## Compile
`bump` compiles files with this command:
```console
$ g++-12 -std=c++17 -pedantic-errors -Wall -Wextra -Weffc++ -Wsign-conversion -Werror-fmax-errors=1 -o $EXECUTABLE_PATH $SRC_PATH
```
This can be changed by editing the `cmd` variable near the top of the file.
