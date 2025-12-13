from utils.hash import md5


def password(doorid: str):
    passw = []
    for i in range(999999999999):
        tmphash = md5(doorid + str(i))
        if tmphash.startswith("00000"):
            passw.append(tmphash[5])
            print(i, tmphash)
            if len(passw) == 8:
                break
    return "".join(passw)


def password2(doorid: str):
    passw = [" "] * 8
    for i in range(999999999999):
        tmphash = md5(doorid + str(i))
        if tmphash.startswith("00000"):
            pos = tmphash[5]
            try:
                if int(pos) < 8 and passw[int(pos)] == " ":
                    passw[int(pos)] = tmphash[6]
            except:  # noqa
                pass
            print(i, tmphash)
            if " " not in passw:
                break
    return "".join(passw)


# print(password2("abc"))
# print(password2("ojvtpuvg"))s
