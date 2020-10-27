RSA Encryption

----DESCRIPTION AND INSTRUCTIONS----

The included program implements RSA encryption in Python 3. The algorithm works by
examining the contents of the file ‘message.txt’ to obtain the plaintext to be encrypted. Next
the program encrypts the message character by character and stores the result in the file
‘ciphertext.txt’. Finally, the program decrypts the generated ciphertext and stores the result in
‘decrypted_message.txt’ After doing so the program checks to make sure that the contents of
‘message.txt’ and ‘decrypted_message.txt’ match to assure the algorithm functions correctly.

In order to create the program four modules were creates: rsa_driver.py, keysetup.py,
encryption.py, and decryption.py. The first one, rsa_driver.py, is simply just the driver code to
initiate the actions and algorithms implemented in the other modules. First the driver runs the
function setkeys() in order the establish a public and private key. This public key is generated
through a function that generates large random integers of a specified length and a function to
make sure that the chosen integers are prime using the Fermat primality test. The private key is
calculated given the public key with the extended Euclidean algorithm implemented to
calculate multiplicative modular inverses. The establishing of these keys requires fast modular
exponentiation to be done for very large integers. Now that the keys are generated the driver code
begins the encryption algorithm to parse the plaintext character by character and implement the function
𝑐 = 𝑀^𝑒[𝑛] where n and e comprise the public key, M is a character of plaintext, and c is a character of
ciphertext. Next the program implements decryption on each generated c value according to the function
𝑀 = 𝑐^𝑑[𝑛] where M, c, and n are as they were previously, but d is the private key. After
decryption and storage, the driver program opens both the original plaintext and the decrypted
plaintext and does a direct comparison between the two strings to verify that the RSA
algorithm was carried out correctly. If so, it prints to the console that it was a success.
Otherwise, it prints that it was a failure to console.

To verify the correctness of the program the requested message was run through the
program. Once the run finished the program indicated that it was a success. Additionally, a
manual check of the two text files was performed to ensure the check algorithm was correct.

To execute the program, make sure the following files are in the same folder:
rsa_driver.py, keysetup.py, encryption.py, decryption.py, and message.txt. The other text files
will be created by the program and will appear in the folder location of the program. Once
made sure of, run the rsa_driver.py file with your Python 3 handler of choice. The creation and
testing of these files was done using the Spyder IDE from Anaconda in Python 3.7.