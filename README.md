# alais

Alaises for your terminal typos

`pip install --user alais`

<br>

### install alaises
`alais me`

### remove alaises
`alais me-not`

### how it works
Add aliases to .bash_aliases

### todo
* source .bashrc so no need to reload terminal
* support for when an alias is removed from alais, should purge any non-existent aliases after preamble
* add functions as aliases to do the reverse of a normal alias (e.g. stop: `sudo rm -rf /`)

### PR's welcome
Restrictions
* aliases must not conflict with an installable program (e.g. apt/yum install) from standard repos.

