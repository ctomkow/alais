# Craig Tomkow, 2023

# local imports
from alais.version import __version__

# python imports
from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter, Namespace
from re import sub
from typing import Dict


def entrypoint():

    parser = _flags(__version__)
    args = parser.parse_args()
    _parse_input(args)


def _flags(version: str) -> ArgumentParser:

    parser = ArgumentParser(
        prog='alais',
        formatter_class=RawDescriptionHelpFormatter,
        description="""
An alais for your terminal typos

> alais me
> alais me-not
""")
    # all flags here
    parser.add_argument('-v', '--version', action='version', version=f"%(prog)s {version}")
    sub_parser = parser.add_subparsers()
    key = sub_parser.add_parser('me', description='Install the alais')
    key.add_argument('me', action='store_true')
    key = sub_parser.add_parser('me-not', description='Install the alais')
    key.add_argument('me-not', action='store_true')

    return parser


def _parse_input(args: Namespace) -> None:

    bash_aliases = Path(Path.home(), '.bash_aliases')

    if 'me' in args:
        _add_preamble(bash_aliases)
        _add_aliases(custom_aliases, bash_aliases)
        print("alais'd!")
    elif 'me-not' in args:
        _remove_aliases(custom_aliases, bash_aliases)
        print("unalais'd!")


# idempotent
def _add_preamble(bash_aliases: Path) -> None:

    if not _line_exists_in_file('# written by alais\n', bash_aliases):
        bash_aliases.write_text('# written by alais\n')


# idempotent
def _add_aliases(aliases: Dict, bash_aliases: Path) -> None:

    with bash_aliases.open('a') as fp:
        for k, v in aliases.items():
            alias = f"alias {k}='{v}'\n"
            if not _line_exists_in_file(alias, bash_aliases):
                fp.write(alias)


# todo: _remove_preamble

# todo: must be idempotent
def _remove_aliases(aliases: Dict, bash_aliases: Path) -> None:

    with bash_aliases.open('r') as f:
        user_bash_aliases = f.readlines()

    with bash_aliases.open('w') as f:
        for line in user_bash_aliases:
            f.write(sub(r"^# written by alais\n$", "", line))

    for k, v in aliases.items():
        with bash_aliases.open('r') as f:
            user_bash_aliases = f.readlines()
        with bash_aliases.open('w') as f:
            for line in user_bash_aliases:
                f.write(sub(fr"^alias {k}='{v}'\n$", "", line))


def _line_exists_in_file(elem: str, file: Path) -> bool:

    if not file.exists():
        return False
    with file.open('r') as fp:
        lines = fp.readlines()
    for line in lines:
        if elem == line:
            return True
    return False


# thanks chatGPT!
custom_aliases = {
    'clera': 'clear',
    'claer': 'clear',
    'celar': 'clear',
    'cler': 'clear',
    'cear': 'clear',
    'gerp': 'grep',
    'greap': 'grep',
    'grpe': 'grep',
    'igt': 'git',
    'gi': 'git',
    'got': 'git',
    'jit': 'git',
    'gti': 'git',
    'sodo': 'sudo',
    'sudu': 'sudo',
    'sodo': 'sudo',
    'sduo': 'sudo',
    #'sl': 'ls',
    'lls': 'ls',
    'lis': 'ls',
    'cv': 'cd',
    'cx': 'cd',
    'cds': 'cd',
    'mkidr': 'mkdir',
    'mkrdir': 'mkdir',
    'makedir': 'mkdir',
    'makdir': 'mkdir',
    'mdir': 'mkdir',
    'mroe': 'more',
    'pign': 'ping',
    'pang': 'ping',
    'pnig': 'ping',
    'pimg': 'ping',
    'comod': 'chmod',
    'chomd': 'chmod',
    'chmode': 'chmod',
    'chmoe': 'chmod',
    'tarr': 'tar',
    'tare': 'tar',
    'atr': 'tar',
    'eixt': 'exit',
}
