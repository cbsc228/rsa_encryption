#this module serves as the driver code for the RSA algorithm

import keysetup as ks
import encryption as encrypt
import decryption as decrypt

#set up the public and private keys
print("Setting public and private keys...")
ks.setKeys()

#get the public key from file
fin = open("public_key.txt", "rt")
publicKey = fin.read()
publicKey = publicKey.split(",")
fin.close()

#encyrypt the message stored in file message.txt, send to ciphertext.txt
print("Encrypting message...")
encrypt.encryptMsg(publicKey[0], publicKey[1])

print("Decrypting message...")
#decrypt the message store in file ciphertext.txt, send to decrypted_message.txt
decrypt.decryptMsg(publicKey[0])

#perform check to verify the decrypted message matches the given message
finCheck1 = open("message.txt", "rt")
finCheck2 = open("decrypted_message.txt", "rt")
if (finCheck1.read() == finCheck2.read()):
    print("Success: message.txt matches decrypted_message.txt")
else:
    print("Failure: message.txt does not match decrypted_message.txt")