"""Day 4 - Pasword checker"""

import pass_checker_04 as pwc

if __name__ == "__main__":
    test_pass_list = ["111111", "223450", "123789"]

    for p in test_pass_list:
        if pwc.is_pw_valid(p):
            print(p, "is VALID")
        else:
            print(p, "is NOT VALID")

    # 168630-718098
    lo = 168630
    hi = 718098

    pcount = 0
    for i in range(lo, hi+1):
        pw = str(i)
        if pwc.is_pw_valid(pw):
            pcount += 1

    # 1686
    print("\nPart 1 - Count of possible passwords is {}".format(pcount))

    # Part 2 - need exactly 2 consecutive digits
    pcount = 0
    for i in range(lo, hi+1):
        pw = str(i)
        if pwc.is_pw_valid2(pw):
            pcount += 1

    # 1145
    print("\nPart 2 - Count of possible passwords is {}".format(pcount))
