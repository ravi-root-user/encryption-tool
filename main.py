import mont
import rsa
import os

# print(mont.if_is_linux())
(public_key, private_key) = rsa.newkeys(2048)
def make_keys():

    with open("public.pem","wb") as f:
        f.write(public_key.save_pkcs1("PEM"))


    with open("private.pem","wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


def read_keys():
    with open("public.pem","rb") as f:
        public_key=rsa.PublicKey.load_pkcs1(f.read())
    with open("private.pem","rb") as f:
        private_key=rsa.PrivateKey.load_pkcs1(f.read())
make_keys()
read_keys()
msg="hello from ravi bansal"
enc_msg=rsa.encrypt(msg.encode(),public_key)

with open("encrypteddata","wb") as f:
    f.write(enc_msg)
    os.system("mv encrypteddata ./encrypted_files")




