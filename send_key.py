import os
import mont as mnt
import subprocess

def send_private():
    try:
        mnt.if_is_linux()
        inputs=int(input("Select your storage device:- "))
        # os.system("mv ./private.pem ")
        moving_file_location=mnt.devices[inputs]
        os.system(f"cp ./private.pem {moving_file_location}")
        a=subprocess.check_output("echo $?",shell=True,text=True).strip()
        if a=='0':
            print("file moved successfully!!")
    except Exception as e:
        print("file not moved")

send_private()