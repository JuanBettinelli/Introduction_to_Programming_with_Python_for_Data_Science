import re

def valid_pw(passw: str) -> bool:
    """checks whether passwords have a valid form.

    Arguments:
        passw: the newly entered password.
    """
    special_chars = [',', '.', '!',
                     '@', '#', '$',
                     '_', '-', '^',
                     '&', '*']
    if passw == "cancel":
        print("Aborted...")
        return True
    elif len(passw) < 8:
        return False
    elif passw.startswith("#") or passw.endswith(" "):
        return False
    elif '\\' in passw or '%' in passw or ':' in passw:
        return False
    elif sum([c in special_chars for c in passw]) < 3:
        return False
    elif sum([x.isdigit() for x in passw]) < 1:
        return False
    elif len(re.findall("[,.!@#$_\-\^&*]{2,}", passw)) > 0:
        # this checks for co-located special characters
        # it uses regular expressions which is great if
        # you find some time to learn it
        # (I never fully learnt it and regret it from time to time)
        return False
    else:
        return not passw.islower()

def main():
    """actual app that runs the code"""
    # Example of the walrus operator which was introduced in python 3.8
    # while  (inp := input("Please enter your password. Enter 'cancel' to abort")) != "cancel" and not valid_pw(inp):
    # the following implementation is used due to the concise form
    # Bonus points, if you have found the getpass functionality
    while not valid_pw(getpass("Please enter your new password. Enter 'cancel' to abort.\n")):
        print("Please try again.")

if __name__ == "__main__":
    main()

"""
In case you want to test some examples:

test_pws = ["thisIs7",  # False
            "ThisStill_isWr0ng!",  # False
            "#violated_St4rT!",  # False
            "Adds4N.Sp4c3_toTh3End! ",  # False
            "Thi5_Should-w9rK!",  # True
            "$thi5_should-not^w9rk!",  # False
            "Thi5_n0t_Should-w9rK!!",  # False
            "^$#@Thi5_n0t_Should-w9rK!!",  # False
            "ch4r_not_Allo%d!",  # False
            "ch4r_not_Allo:d!",  # False
            "ch4r_not_Allo\d!",  # False
            "____not_All9wed!",  # False
            "12345678!9#10A_",  # True
            "???no_spec 4 ? Signs#should_go",  # True
            ",t!h.s-i^s@v4L#i_D*"]   # True

for test in test_pws:
    print(f"{test:<30s}", ": ", password(test))

"""