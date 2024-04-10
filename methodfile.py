# Anders Swenson
from Labs.Lab_9.Lab9_3502.Scratch import decode
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encode(instring):
    retstr = ""
    simlist = []
    simlist.extend(instring)
    for strchar in simlist:
        intchar = int(strchar)
        if (intchar + 3) >= 10:
            retstr += str((intchar + 3) - 10)
        else:
            retstr += str(intchar + 3)
    return retstr

if __name__ == "__main__":
    menu()
    loop = True
    while loop:
        MenuOpt = int(input("Please enter an Option: "))
        if MenuOpt == 1:
            passin = input("Please enter your password to encode: ")
            newpass = encode(passin)
            print("Your password has been encoded and stored!\n")
        elif MenuOpt == 2:
            print(f"The encoded password is {newpass}, and the original password is {decode(newpass)}.\n")
        elif MenuOpt == 3:
            quit()
        menu()

