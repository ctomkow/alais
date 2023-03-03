# Craig Tomkow, 2023
#
# python imports
import os
from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter, Namespace
from re import sub


def entrypoint():

    version = _read_version()
    parser = _flags(version)
    args = parser.parse_args()
    _parse_input(args)


def _read_version() -> str:

    # read from the VERSION file
    with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version_file:
        version = version_file.read().strip()
    return version


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

    if 'me' in args:
        _install(custom_aliases)
        print("alais'd!")
    elif 'me-not' in args:
        _uninstall(custom_aliases)
        print("unalais'd!")


# must be idempotent
def _install(aliases: dict) -> None:

    with Path(Path.home(), '.bash_aliases').open('a') as f:
        f.write('\n')
        f.write('# written by alais\n')
        for k, v in aliases.items():
            f.write(f"alias {k}='{v}'\n")


# must be idempotent
def _uninstall(aliases: dict) -> None:

    with Path(Path.home(), '.bash_aliases').open('r') as f:
        user_bash_aliases = f.readlines()

    with Path(Path.home(), '.bash_aliases').open('w') as f:
        for line in user_bash_aliases:
            f.write(sub(r"^# written by alais\n$", "", line))

    for k, v in aliases.items():
        with Path(Path.home(), '.bash_aliases').open('r') as f:
            user_bash_aliases = f.readlines()
        with Path(Path.home(), '.bash_aliases').open('w') as f:
            for line in user_bash_aliases:
                f.write(sub(fr"^alias {k}='{v}'\n$", "", line))


# thanks chatGPT!
custom_aliases = {
    'clera': 'clear',
    'claer': 'clear',
    'celar': 'clear',
    'cler': 'clear',
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
