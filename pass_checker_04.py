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

def is_pw_valid2(pw):
    """Part 2 validation - there has to be a 2-digit match that is not part of a larger match"""

    # must be 6 chars
    if len(pw) != 6:
        return False

    # reading from left to right, the digits never decrease
    for idx in range(5):
        if pw[idx+1] < pw[idx]:
            return False

    # must have 2 matching digits
    dig_cnt = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for num in pw:
        dig_cnt[num] += 1

    has_two = False
    for digit in list(dig_cnt.keys()):
        if dig_cnt[digit] == 2:
            has_two = True

    return has_two
