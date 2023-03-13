# alais

Aliases for your terminal typos

`pip install --user alais`

**or** install the bleeding edge version

`pip install --user git+https://github.com/ctomkow/alais.git`

<br>

## add aliases
1. `alais add`
2. `. .bashrc`

## remove aliases
1. `alais remove`
2. reload terminal

## how it works
Copies .alais to home directory. Adds an entry to .bashrc to source the file

### shell alias
.alais contains `alias`es to fix common typos of *nix tools.

e.g. you can type `clera` and your terminal will execute the `clear` command.

See the .alais file in your home directory for all aliases.

### shell functions
.alais also contains functions to fix sub-command typos and to protect yourself from a destructive typo.

e.g. It parses the `sudo` command matching on `rm -rf /` and `rm -fr /`. If it matches, it outputs `pls no` then exits, else, your command continues as normal.

## PR's welcome
Restrictions
* aliases must not conflict with an installable program (e.g. apt/yum install) from standard repos.
