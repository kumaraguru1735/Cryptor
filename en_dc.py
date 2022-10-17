import base64
import cryptocode

def ency(plain_text):
    plain_text_bytes = plain_text.encode("ascii")
    base64_ency_bytes = base64.b64encode(plain_text_bytes)
    base64_ency = base64_ency_bytes.decode("ascii")
    pass_ency = input("Enter the password to encrypt: ")
    c_encoded = cryptocode.encrypt(base64_ency,pass_ency)
    print("===ENCRYPTED TEXT====\n",c_encoded)

def decy(ency_text):
    pass_decy = input("Enter the password to decrypt: ")
    c_decoded = cryptocode.decrypt(ency_text, pass_decy)
    if(c_decoded == False):
        print("Invalid Hash or password is wrong")
    else:
        c_decoded_bytes = c_decoded.encode("ascii")
        base64_decy_bytes = base64.b64decode(c_decoded_bytes)
        base64_decy = base64_decy_bytes.decode("ascii")
        print("===DECRYPTED TEXT===\n",base64_decy)

option_ch = input("\n 1.Encryption \n 2.Decryption\n Choose any one of the option: ")

if(option_ch == "1"):
    plain_text = input("Enter the text to encrypt: ")
    ency(plain_text)
elif(option_ch == "2"):
    ency_text = input("Enter the hash to decrypt: ")
    decy(ency_text)
else:
    print("Error choose the correct option")
