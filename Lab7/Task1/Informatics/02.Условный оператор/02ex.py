

x = int(input())
def answer(x):
    yes = "YES"
    no = "NO"
    # if x % 4 == 0 :
    #     # if x % 100 != 0:
    #     #     return yes
    #     return yes
    # else:
    #     return no
    
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return "YES"
            else:
                return "NO"
        else:
            return "YES"
    else:
        return "NO"
ans = answer(x)
print(ans)