def palind(r):
    e = len(r)-1
    s = 0
    while (e > s):
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True

r = (1, 2, 3, 3, 5, 4)
if (palind(r)):
 print("This word is a flip flop!")
else:
    print("This word is not a flip flop!")