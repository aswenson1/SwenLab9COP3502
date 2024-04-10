print("Hello world!")

def decode(pw):
    newstr = ""
    for i in pw:
        newnum = int(i) - 3
        if newnum < 0:
            newstr += str((newnum) + 10)[-1]
        else:
            newstr += str(newnum)[-1]
    
    return newstr
