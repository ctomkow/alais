
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


def test_install_aliases(aliases: Dict, bash_aliases: Path):

    main._install_aliases(aliases, bash_aliases)
    with bash_aliases.open() as fp:
        for i, line in enumerate(fp):
            assert line == f"alias {list(aliases)[i]}='{list(aliases.values())[i]}'\n"
    bash_aliases.unlink()
