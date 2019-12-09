"""Password Checker
Count how many 6-digit passwords in a range are valid"""


def is_pw_valid(pw):
    """Does this password follow all the rules?"""

    # must be 6 chars
    if len(pw) != 6:
        return False

    # 2 consec digits must match
    cmatch = 0
    for idx in range(5):
        if pw[idx] == pw[idx+1]:
            cmatch += 1
            break

    if cmatch == 0:
        return False

    # reading from left to right, the digits never decrease
    for idx in range(5):
        if pw[idx+1] < pw[idx]:
            return False

    return True