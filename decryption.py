#this module serves to decrpty ciphertext in the RSA algorithm
from keysetup import modExp

#decrypt the message stored in ciphertext.txt
#input: n from public key pair (n, e)
#sends calculated plaintext to decrypted_message.txt
def decryptMsg(n):
    #retrieve the private key from file for decryption
    fin = open("private_key.txt", "rt")
    d = fin.read()
    fin.close()
    #holds the plaintext after decryption
    plaintext = ""
    #retrieve the ciphertext from file
    fin = open("ciphertext.txt", "rt")
    ciphertext = fin.read()
    ciphertext = ciphertext.split(",")
    #decrypt each separated value of ciphertext  and add to plaintext
    for i in range(len(ciphertext)):
        plaintext += str(pow(int(ciphertext[i]), int(d), int(n)))
    fin.close()
    #write the decrypted plaintext to file
    fout = open("decrypted_message.txt", "w")
    fout.write(plaintext)
    fout.close()