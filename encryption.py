#this module serves to encrypt messages in the RSA algorithm 
from keysetup import modExp

#encrypt the message stored in message.txt
#input: public key pair (n ,e)
#sends calculated ciphertext to ciphertext.txt
def encryptMsg(n, e):
    #holds the ciphertext
    ciphertext = ""
    #open the plaintext file
    fin = open("message.txt", "rt")
    plaintext = fin.read()
    #encrypt each character as comma separated values
    for i in range(len(plaintext)):
        if i != len(plaintext) - 1:
            ciphertext += str(pow(int(plaintext[i]), int(e), int(n))) + ","
        else:
            ciphertext += str(pow(int(plaintext[i]), int(e), int(n)))
    fin.close()
    #write the generated ciphertext to file
    fout = open("ciphertext.txt", "w")
    fout.write(ciphertext)
    fout.close()