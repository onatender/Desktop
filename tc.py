


tc = 10000000000
def tc_check(tc):
    if type(tc) != int:
        return False
    if tc < 10000000000 or tc > 99999999999:
        return False
    tc_as_str = str(tc)
    res1 = 7*(int(tc_as_str[0])+int(tc_as_str[2])+int(tc_as_str[4])+int(tc_as_str[6])+int(tc_as_str[8]))
    res2 = int(tc_as_str[1])+int(tc_as_str[3])+int(tc_as_str[5])+int(tc_as_str[7])
    hane10= (res1-res2)%10
    if hane10 != int(tc_as_str[9]):
        return False
    hane11 = (int(tc_as_str[0])+int(tc_as_str[1])+int(tc_as_str[2])+int(tc_as_str[3])+int(tc_as_str[4])+int(tc_as_str[5])+int(tc_as_str[6])+int(tc_as_str[7])+int(tc_as_str[8])+int(tc_as_str[9]))%10
    if hane11 != int(tc_as_str[10]):
        return False
    return True

for i in range(10000000000,99999999999):
    if tc_check(i):
        print(i)