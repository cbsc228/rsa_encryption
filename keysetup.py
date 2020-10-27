#this module serves to create the keys for RSA encryption
import random
from math import gcd


#---------
#modExp FAILS TO WORK CORRECTLY DESPITE BEING THE ALGORITHM DIRECTED TOWARDS IN THE CLASS NOTES
#---------
#perform modular exponentiation
#input: the base and exponent to calculate in mod the modulus
#output: the result of the exponentiation
def modExp(base, power, modulus):
    z = 1
    binPower = bin(int(power))
    print(binPower)
    sizePower = len(bin(int(power))) - 1
    for i in range(sizePower, 1, -1):
        print(binPower[i])
        z = (z**2) % int(modulus)
        if binPower[i] == '1':
            z = (z*base) % int(modulus)
    return z
     
#generate a random large integer
#input: the length of bits for the number to be
#output: a randomly generated odd integer of the specified bit length
def randLargeInt(length):
    # generate random bits
    num = random.getrandbits(length)
    #make sure the most significant bit is 1 and the number is odd
    num |= (1 << length - 1) | 1
    return num


#test if the given integer is prime or not with the Fermat Primality Test
#input: number n to test for primality and the number of times to run the probabilistic test
#output: true is n is prime, false if n is composite
def primeTest(n, numTrys):
    #trivial case to make sure of
    if (n == 2):
        return True
    #make sure the number is both positive and odd
    if (n <= 1) or (n % 2 == 0):
        return False
    #perform fermat primality test the given number of times to help ensure we don't give a false positive
    for i in range(numTrys):
        a = random.randint(1, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True
   
 
#perform the extended euclid algorithm to compute modulo inverse
#input: a base to find the inverse of in mod the modulus
#output: inverse of the base in mod the modulus
def modMultInverse(base, modulus):
    origMod = modulus
    #initial coefficients where x will become the inverse
    y = 0
    x = 1
    if (modulus == 1) : 
        return 0
    while (base > 1) :
        #perform extended euclidean algorithm
        quotient = base // modulus 
        holder = modulus 
        modulus = base % modulus 
        base = holder 
        holder = y 
        #ppdate coefficients
        y = x - quotient * y 
        x = holder
    #fix a negative value in mod modulus 
    if (x < 0): 
        x += origMod
    #return the coefficient of base (the inverse)
    return x

#sets the public and private keys for RSA algorithm
#writes public key to public_key.txt
#writes private key to private_key.txt
def setKeys():
    #initialize p and q to arbitrary non-prime numbers
    p = 4
    q = 4
    pLength = 512
    qLength = 1024
    #find a suitable prime p
    while (primeTest(p, 20) == False):
        p = randLargeInt(pLength)
    #find a suitable prime q
    while (primeTest(q, 20) == False):
        q = randLargeInt(qLength)
    #write the public key to file
    e = 2**16 + 1
    while gcd(e, (p-1)*(q-1)) != 1:
        e += 1
    fout = open("public_key.txt", "w")
    fout.write(str(p * q) + "," + str(e))
    fout.close()
    #write the private key to file
    d = modMultInverse(e, (p-1)*(q-1))
    fout = open("private_key.txt", "w")
    fout.write(str(d))
    fout.close()
    return