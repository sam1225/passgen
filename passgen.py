"""
Program Name    : passgen.py
Python version  : python3
Description     : Passgen generates strong passwords using a combination of mix-case chars, numbers, & symbols.
Date            : 26-FEB-2021
"""


import sys
import random
import string


def main():
    val = argument_parsing(sys.argv)
    display(val)


def display(val):
    help_text = """Passgen generates strong passwords using a combination of mix-case chars, numbers, & symbols.
Usage: passgen [OPTION]
  -h, --help                 this message
  <password length>          length between 8 - 60
"""
    if val == "help":
        print(help_text)
    elif val == "no_args":
        print(help_text)
        print("Provide password length or use one of the below passwords:")
        pass1, pass2, pass3 = default_pass()
        print(f"  Short : {pass1}")
        print(f"  Medium: {pass2}")
        print(f"  Long  : {pass3}")
    elif val == "not_num" or val == "num_outside_range":
        print(help_text)
        print("Password length should a number between 8 - 60")
    else:
        passwd = password_generator(val)
        print(f"Your password of length {val}: {passwd}")
    print("")   


def argument_parsing(arg_list):
    args_cnt = len(arg_list) - 1
    if args_cnt == 0:
        return "no_args"
    elif arg_list[1] in ["-h", "--help"]:
        return "help"
    else:
        try:
            pass_len = int(arg_list[1])
        except ValueError:
            return "not_num"
    if pass_len < 8 or pass_len > 60:
        return "num_outside_range"
    return pass_len


def default_pass():
    pass1_len = 12
    pass2_len = 28
    pass3_len = 40
    pass1 = password_generator(pass1_len)
    pass2 = password_generator(pass2_len)
    pass3 = password_generator(pass3_len)
    return (pass1, pass2, pass3)


def password_generator(pass_len):
    lc_list = list(string.ascii_lowercase)
    uc_list = list(string.ascii_uppercase)
    num_list = list(string.digits)
    sym_list = ['!', '#', '$', '%', '&', '(', ')', '*', '<', '>', '?', '@', '[', ']', '^', '{', '}', '~']
    
    all_list = lc_list + uc_list + num_list + sym_list

    type_len = pass_len // 4
    type_rem = pass_len % 4

    p1 = random.sample(lc_list, type_len)
    p2 = random.sample(uc_list, type_len)
    p3 = random.sample(num_list * 2, type_len)
    p4 = random.sample(sym_list, type_len)
    p5 = random.sample(all_list, type_rem)

    p6 = p1 + p2 + p3 + p4 + p5
    random.shuffle(p6)
    
    return "".join(p6) 


if __name__ == "__main__":
    main()    
