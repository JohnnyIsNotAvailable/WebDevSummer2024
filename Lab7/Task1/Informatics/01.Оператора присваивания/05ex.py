s = 109

v = int(input())
t = int(input())

sCurrent = v*t

if sCurrent > 0:
    if sCurrent > s:
        while sCurrent > s:
            sCurrent -= s
    print(sCurrent)
elif sCurrent < 0:
    if abs(sCurrent) > 0:
        while abs(sCurrent) > s:
            sCurrent += s
    print(s + sCurrent)
else:
    print(s)
