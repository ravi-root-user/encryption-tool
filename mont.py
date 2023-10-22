import platform
import os
def is_platform():
    return platform.uname().system


def if_is_linux():
    a=is_platform()
    if a=="Linux":
        print("##################################################################\n \t\tEnternal mounted devices\n")
        print(os.system("df -Th | grep media | awk '{print $NF}'"))
        print("##################################################################")