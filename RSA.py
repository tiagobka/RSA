import random
class RSA:

    def __init__(self):
        pass
        #this is a constructor
    def generatePrimeNumber (self):
        pass

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



c = RSA()
c.rabinMiller(54)
