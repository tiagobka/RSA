import random
class RSA:

    def __init__(self):
        pass
        #this is a constructor

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999]
    def is_prime(self, num):
        if num == 1:
            return False
        if num in self.lowPrimes:
            print(num,"is a prime number")

        if num > 2000:
            for prime in self.lowPrimes:
                if (num%prime == 0):
                    print(num,"is not a prime number")
            if (self.rabinMiller(num) == True):
                print("isprime")
            else:
                print("is not prime")
            #return self.rabinMiller(num)
        else:
            print(num,"is a prime number")

    def generatePrimeNumber (self,size):
        while True:
            num = random.randrange(2**(size-1), 2**(size))
            if self.is_prime(num):
                return num;


    def RSA_Algorithm(self):
        pass
        q =13
        p = 5

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
                        j = i + 1
                        v = (v ** 2) % num
            return True # it is likely a prime



def main():
     c = RSA()
     c.is_prime(2778)

main()
