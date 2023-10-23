import platform
import subprocess as sb
def is_platform():
    return platform.uname().system

def if_is_linux():
    global devices  
    a = is_platform()
    if a == "Linux":
        print("##################################################################\n \t\tExternal mounted devices\n")
        output = sb.check_output("df -Th | grep media | awk '{print $NF}'", shell=True)
        devices = output.decode('utf-8').strip().split('\n')
        for i, device in enumerate(devices):
            print(f"Device {i + 1}: {device}")
        print("##################################################################")