
unlock
======


**Unlock the specified keychain.**
### Usage
```bash
keychain unlock [-h] [-s] [-v] [--no-color] [--log-stream STREAM]
    [-p PATH]
    [-pw PASSWORD]
```
### Optional arguments for action `unlock`

##### `-pw, --password=PASSWORD`


Keychain password. Alternatively to entering PASSWORD in plaintext, it may also be specified using a "@env:" prefix followed by a environment variable name, or "@file:" prefix followed by a path to the file containing the value. Example: "@env:<variable>" uses the value in the environment variable named "<variable>", and "@file:<file_path>" uses the value from file at "<file_path>". [Default: '']
### Optional arguments for command `keychain`

##### `-p, --path=PATH`


Keychain path. If not provided, the system default keychain will be used instead
### Common options

##### `-h, --help`


show this help message and exit
##### `-s, --silent`


Disable log output for commands
##### `-v, --verbose`


Enable verbose logging for commands
##### `--no-color`


Do not use ANSI colors to format terminal output
##### `--log-stream=stderr | stdout`


Log output stream. Default `stderr`