import random
class RSA:
    def __init__(self, keySize:int = 1024):
        self.P = 0
        self.Q = 0
        self.z = 0
        self.n = 0
        self.keySize = keySize
        self.lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093,
                 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
                 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327,
                 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481,
                 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597,
                 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721,
                 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867,
                 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997,
                 1999]



    def is_prime(self, num):
        if num == 1:
            return False
        if num in self.lowPrimes:
            return True

        if num > 2000:
            for prime in self.lowPrimes:
                if (num%prime == 0):
                    #print(num,"is not a prime number")
                    return False
            if (self.rabinMiller(num) == True):
                #print("isprime")
                return True
            else:
                #print("is not prime")
                return False
            #return self.rabinMiller(num)
        else:
            return False
            #print(num,"is a prime number")

    #def generatePrimeNumber (self):
    #    while True:
    #        num = random.randrange(2**(self.keySize-1), 2**(self.keySize))
    #        if self.is_prime(num):
    #            return num


    def RSA_Algorithm(self):
        self.setPPrime() #gets a prime number P with lenght of keySize
        self.setQPrime() #gets a prime number Q with lenght of keySize
        self.n = self.P * self.Q
        self.z = (self.P-1)*(self.Q-1)

        while True:
            self.publicKey = random.randrange(2 ** (self.keySize - 1), 2 ** (self.keySize))
            if self.gcd(self.publicKey, self.z) == 1:
                break

        self.privateKey = self.findModInverse(self.publicKey, self.z)

    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def findModInverse(self, a, m):
        if self.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m


    #This function checks tells if there is a probability of a number being prime
    #if a number is composit it will return fa
    def rabinMiller(self, num):
        #Step1)Find n-1 = 2^i *m where i and m are integers
        #Step2)pick a value a such that 1<a < n-1
        #Step3)compute b0 = a^m(modn), if needed compute bi = (bi-1)^2
        #---------STEP1
        nm1 = num - 1
        i = 1
        m =nm1

        while m % 2 == 0:
           m = m // 2
           i += 1
        #while isinstance(nm1%pow(2,i),int): It does not work
        #    m = nm1//pow(2,i)
        #    i +=1
        #----------STEP1-END

        for trials in range(5):
            a = random.randrange(2, num - 1)
            v = pow(a, m, num)#a^m (mod n), it is computed more efficiently than pow(x, y) % z)
            if v != 1:
                j = 0
                while v != (num - 1):
                    if j == i - 1:
                        return False # it is composite
                    else:
                        j = j + 1
                        v = (v ** 2) % num
            return True # it is likely a prime


    def generateLargePrime(self):
        while True:
            num = random.randrange(2**(self.keySize-1), 2**(self.keySize))
            if self.is_prime(num):
                return num

    def encryptInt(self, msg:int):
        ret = pow(msg,self.publicKey,self.n)
        return ret

    def encryptText(self, msg:str):
        # (keyLen/8*2)-1 is the max num of bytes that a key of length "keyLen" can successfully encrypt
        # using built in pow function.
        bufferSize = ((self.keySize//8)*2)-1 #e.g. a 1024 key can encrypt 255 bytes at a constant time.

        ret = str()
        while (len(msg)!=0):
            if len(msg) > bufferSize:
                buffer = msg[0:bufferSize]
                msg = msg[bufferSize:]
                separator = "a"
            else:
                buffer = msg
                msg = ""
                separator = ""

            first_letter = buffer[0]
            char = ord(first_letter)
            hexad = hex(char)
            out = str(hexad)[2:]
            for c in buffer[1:]:
                add = hex(ord(c))
                addstr = str(add)[2:]
                if len(addstr) ==1:
                    addstr = "0" + addstr
                out = str(out) + addstr
            hexa = int(out, 16)

            ret += str(pow(hexa,self.publicKey,self.n)) + separator
        return ret

    def decryptInt(self, crypted):
        ret = pow(crypted,self.privateKey,self.n)
        return ret

    def decryptText(self, crypted:str):
        ret = str()
        while (len(crypted) != 0):
            index = crypted.find("a")
            if (index > 0):
                buffer = int(crypted[0:index])
                crypted = crypted[index+1:]
            else:
                buffer = int(crypted)
                crypted = ""

            crypt = pow(buffer, self.privateKey, self.n)
            hexa = hex(crypt)
            crypt = str(hexa)[2:]


            for i in range(0,len(crypt),2):
                num = int(crypt[i:i+2],16)
                ret += chr(num)
        return ret

    def encryptTextFile(self, inputFile:str, outputFile:str):
        bufferSize = ((self.keySize // 8) * 2) - 1
        file_object = open(inputFile,"r")
        while True:
            data = file_object.read(bufferSize)
            if not data:
                break

            first_letter = data[0]
            char = ord(first_letter)
            hexad = hex(char)
            out = str(hexad)[2:]
            for c in data[1:]:
                add = hex(ord(c))
                addstr = str(add)[2:]
                if len(addstr) ==1:
                    addstr = "0" + addstr
                out = str(out) + addstr
            hexa = int(out, 16)

            ret = str(pow(hexa, self.publicKey, self.n))
            toFile = open(outputFile, "a")
            toFile.write(ret)
            toFile.write("\n")
            toFile.close()

        file_object.close()

    def decryptTextFile(self, inputFile: str, outputFile: str):
        file_object = open(inputFile, "r")
        while True:

            buffer = file_object.readline()
            if not buffer:
                break
            ret = str()
            crypt = pow(int(buffer), self.privateKey, self.n)
            hexa = hex(crypt)
            crypt = str(hexa)[2:]

            for i in range(0, len(crypt), 2):
                num = int(crypt[i:i + 2], 16)
                ret += chr(num)
            toFile = open(outputFile, "a")
            toFile.write(ret)
            #toFile.write("\n")
            toFile.close()





    def createPublicKeyFile(self, fileName:str = "./keys/publicKeyFile.txt"):
        file = open(fileName, "w")
        file.write(str(self.publicKey))
        file.write(":")
        file.write(str(self.n))
        file.close()
    def createPrivateKeyFile(self, fileName:str = "./keys/privateKeyFile.txt"):
        file = open(fileName, "w")
        file.write(str(self.privateKey))
        file.write(":")
        file.write(str(self.n))
        file.close()
    def getPrivateKeyFromFile(self, fileName:str = "./keys/privateKeyFile.txt"):
        file = open(fileName, "r")
        line = file.readline()
        file.close()
        try:
            field= line.split(":")
            self.privateKey = int(field[0])
            self.n = int(field[1])
        except():
            print ("Invalid private key file")
    def getPublicKeyFromFile(self, fileName:str = "./keys/publicKeyFile.txt"):
        file = open(fileName, "r")
        line = file.readline()
        file.close()
        try:
            field= line.split(":")
            self.publicKey = int(field[0])
            self.n = int(field[1])
        except():
            print ("Invalid public key file")

    def setPPrime(self):
        self.P = self.generateLargePrime()

    def setQPrime(self):
        self.Q = self.generateLargePrime()

    def setKeySize(self, keySize:int):
        if keySize <8 or keySize > 2048:
            raise Exception("RSA key length should be larger than 7 and smaller than 2049.")
        self.keySize = keySize
