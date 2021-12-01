----
### Passgen (Password Generator)

Passgen is tool that generates strong passwords for you using a mix of ASCII charaters.
It uses a mix of lowercase/uppercase charaters, numbers, and symbols to generate the 
passwords. The user need to provide a password length as a command line argument.
If password length is not provided, the tool generates three passwords to choose from.

***It is written in Python 3.***

[Repository Link](https://github.com/sam1225/passgen)

```markdown
$ python3 passgen.py
Passgen generates strong passwords using a combination of mix-case chars, numbers, & symbols.
Usage: passgen [OPTION]
  -h, --help                 this message
  <password length>          length between 8 - 60

Provide password length or use one of the below passwords:
  Short : 1KB#2]}Yf0ug
  Medium: 8}0iEJw23v^u>OCjz)RU$#{K49o4
  Long  : ?WQ3(U#1{]9yk8OvJNXt@5&B~7c6sqChP^47!b5e

$ python3 passgen.py 35
Your password of length 35: V#2T]dc}Cr$zxaOok816EK(6[0Pzk^e?M21

```
