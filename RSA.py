import random
class RSA:
    def printTest(self):
        print("Hello World!")

    def __init__(self):
        pass
        #this is a constructor
    def generatePrimeNumber (self):
        pass

    def RSA_Algorithm(self):
        pass
        q =13
        p = 5

    def rabinMiller(self, num):
        #Find n-1 = 2^k *m where k and m are integers
        #pick a value a such that 1<a < n-1
        s = num - 1
        t = 0

        while s % 2 == 0:
            s = s // 2
            t += 1
        for trials in range(5):
            a = random.randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1:
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
            return True

    def is_prime(num):
        if num > 1:
            for i in range (2,num):
                if (num%i) == 0:
                    print(num,"is not a prime number")
                    break
        else:
            print(num,"is a prime number")
c = RSA()
c.printTest()
