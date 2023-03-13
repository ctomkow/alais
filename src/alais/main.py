# Craig Tomkow, 2023

# local imports
from alais.version import __version__

# python imports
from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter, Namespace
from re import escape, sub
from typing import List
from shutil import copy


def entrypoint():

    parser = _flags(__version__)
    args = parser.parse_args()
    _parse_input(args)


def _flags(version: str) -> ArgumentParser:

    parser = ArgumentParser(
        prog='alais',
        formatter_class=RawDescriptionHelpFormatter,
        description="""
Aliases for your terminal typos

> alais add
> alais remove

How it works
------------
It copies .alais to your home directory. This contains aliases and functions. Aliases are used to fix common
typos. Functions are used to protect you from the bad effects of typos.
""")
    # all flags here
    parser.add_argument('-v', '--version', action='version', version=f"%(prog)s {version}")
    sub_parser = parser.add_subparsers()
    key = sub_parser.add_parser('add', description='Add the aliases')
    key.add_argument('add', action='store_true')
    key = sub_parser.add_parser('remove', description='Remove the aliases')
    key.add_argument('remove', action='store_true')

    return parser


def _parse_input(args: Namespace) -> None:

    bashrc = Path(Path.home(), '.bashrc')
    alais = Path(Path(__file__).resolve().parents[0], '.alais')

    shell_code_to_source_alais = [
        'if [ -f ~/.alais ]; then # written by alais\n',
        '    . ~/.alais # written by alais\n',
        'fi # written by alais\n'
    ]

    if 'add' in args:
        _copy_file(alais, Path.home())
        _append_to_file_safely(shell_code_to_source_alais, bashrc)
        print(".alais installed and .bashrc modified")
    elif 'remove' in args:
        _delete_file_safely(Path(Path.home(), '.alais'))
        _delete_from_file(shell_code_to_source_alais, bashrc)
        print(".alais deleted and .bashrc modifications reverted")


def _copy_file(file: Path, dest: Path) -> None:

    copy(file.absolute().as_posix(), dest.absolute().as_posix())


def _delete_file_safely(file: Path) -> None:

    if file.exists():
        file.unlink()

# this is idempotent
def _append_to_file_safely(text: List[str], file: Path) -> None:

    with file.open('a') as fp:
        for line in text:
            if not _line_in_file(line, file):
                fp.write(line)


def _delete_from_file(text: List[str], file: Path) -> None:

    for line in text:
        with file.open('r') as fp:
            file_lines = fp.readlines()
        with file.open('w') as fp:
            for existing_line in file_lines:
                print(escape(line))
                fp.write(sub(fr"^{escape(line)}$", '', existing_line))


def _line_in_file(elem: str, file: Path) -> bool:

    if not file.exists():
        return False
    with file.open('r') as fp:
        lines = fp.readlines()
    for line in lines:
        if elem == line:
            return True
    return False
