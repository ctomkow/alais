
# local imports
from alais import main

# python imports
import os
from typing import List
from pathlib import Path

# 3rd party imports
import pytest


@pytest.fixture
def setup():

    # set working dir to tests directory to read from .bash_aliases
    os.chdir(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def shell_code() -> List[str]:

    return [
        'if [ -f ~/.alais ]; then # written by alais\n',
        '    . ~/.alais # written by alais\n',
        'fi # written by alais\n'
    ]

@pytest.fixture
def test_file() -> Path:

    return Path('.test_file')


# todo: test_copy_file

def test_delete_file_safely(test_file):

    test_file.write_text('test')
    main._delete_file_safely(test_file)
    assert not test_file.exists()


def test_append_to_file_safely(shell_code, test_file):

    main._append_to_file_safely(shell_code, test_file)
    main._append_to_file_safely(shell_code, test_file)
    with test_file.open() as fp:
        assert len(fp.readlines()) == 3
    test_file.unlink()


def test_delete_from_file(shell_code, test_file):

    main._append_to_file_safely(shell_code, test_file)
    main._delete_from_file(shell_code, test_file)
    assert test_file.read_text() == ''
    test_file.unlink()


def test_line_in_file(test_file):

    test_file.write_text('test string')
    assert main._line_in_file('test string', test_file)
    test_file.unlink()

def test_line_in_file_not(test_file):

    test_file.write_text('no string')
    assert not main._line_in_file('no match', test_file)
    test_file.unlink()