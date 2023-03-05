
# local imports
from alais import main

# python imports
import os
from typing import Dict
from pathlib import Path

# 3rd party imports
import pytest


@pytest.fixture
def setup():

    # set working dir to tests directory to read from .bash_aliases
    os.chdir(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def aliases() -> Dict:

    return {
        'fdsa': 'asdf',
        'asd': 'asdf',
        'asf': 'asdf',
    }

@pytest.fixture
def bash_aliases() -> Path:

    return Path('.bash_aliases')


def test_add_preamble(bash_aliases):

    main._add_preamble(bash_aliases)
    assert bash_aliases.read_text() == '# written by alais\n'
    bash_aliases.unlink()


def test_add_aliases(aliases, bash_aliases):

    main._add_aliases(aliases, bash_aliases)
    with bash_aliases.open() as fp:
        for i, line in enumerate(fp):
            assert line == f"alias {list(aliases)[i]}='{list(aliases.values())[i]}'\n"
    bash_aliases.unlink()


def test_line_exists_in_file(bash_aliases):

    bash_aliases.write_text('test string')
    assert main._line_exists_in_file('test string', bash_aliases)
    bash_aliases.unlink()

def test_line_exists_in_file_no_exists(bash_aliases):

    bash_aliases.write_text('no string')
    assert not main._line_exists_in_file('no match', bash_aliases)
    bash_aliases.unlink()