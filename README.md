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

##### *I do not recommend you to use bump; Makefile and other methods are better. I use it because it is easiest for me.*

## How to use (zsh on Mac)
1. Ensure you have Python3 installed. Then, download the `bump.py` file.
2. Give `bump.py` executable permissions by running `chmod +x path/to/bump.py`
3. Go to your `~/.zshrc` and add `bump="/path/to/bump.py"` to it.
4. Either reload/exit your terminal or type `source ~/.zshrc` to apply the updated configurations for `.zshrc`.

## Commands
```console
$ bump -c $FILE   OR bump --compile $FILE    # Compile `file` if it is in ./src/
$ bump -a         OR bump --all              # Compile every file in ./src/ to ./target/
$ bump -xa        OR bump --clearall         # Delete every executable in ./target/
$ bump -x $FILE   OR bump --clear $FILE      # Delete `file` if it is an executable in ./target/
$ bump OR bump -h OR bump --help             # Help page
```

## Compile
`bump` compiles files with this command:
```console
$ g++-12 -std=c++17 -pedantic-errors -Wall -Wextra -Weffc++ -Wsign-conversion -Werror -fmax-errors=1 -o $EXECUTABLE_PATH $SRC_PATH
```
This can be changed by editing the `cmd` variable near the top of the file.
