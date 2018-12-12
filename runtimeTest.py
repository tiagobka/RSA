from RSA import RSA
from datetime import datetime
import matplotlib.pyplot as plt
from sys import getsizeof
import random


def main():

    nBytes_to_test = [1,2,4,8,16,32,64,128,256,512,1024]

    nKeys_to_test = [ 256, 512,1024, 2048]

    runTimeKeyCreation = list()
    runTimeEncryption = list(list())
    runTimeDecryption = list(list())

    rsa = RSA(16) #starts at keylenght 16
    for j in range(len(nKeys_to_test)):
        rsa.setKeySize(nKeys_to_test[j])   #set key size to current nKeys_to_test
        encryptionTimeList = list()
        decryptionTimeList = list()
        cKs = datetime.now()  #create key start time
        rsa.RSA_Algorithm()
        cKe = datetime.now()  #create key end time
        cKt = (cKe - cKs).total_seconds() #create key time
        runTimeKeyCreation.append(cKt)


        msg = str()
        for i in range(len(nBytes_to_test)):
            while (len(msg)!= nBytes_to_test[i]):
                msg += chr(random.randrange(16, 200))

            eRts = datetime.now() # encryption run time start
            crypt = rsa.encryptText(msg)
            eRte = datetime.now() # encryption run time end
            eMsgT = (eRte-eRts).total_seconds() #encrypt message time

            dRts = datetime.now() #decrypt run time start
            decryptMsg= rsa.decryptText(crypt)
            dRte = datetime.now() #decryption run time end
            dMsgT = (dRte-dRts).total_seconds()

            if (decryptMsg == msg):
                encryptionTimeList.append(eMsgT)
                decryptionTimeList.append(dMsgT)
            else:
                for i, v in enumerate (msg):
                    if v != decryptMsg[i]:
                        file = open("./data/data.txt","a")
                        print ("V:", v,ord(v), "D: ", decryptMsg[i], ord(decryptMsg[i]))
                        file.write("V:" + v + str(ord(v)) + " D: "+ decryptMsg[i] + str(ord(decryptMsg[i]))+ "\n")
                        file.close()
                        break

        runTimeEncryption.append(encryptionTimeList)
        runTimeDecryption.append(decryptionTimeList)


    #plt.plot(nKeys_to_test, runTimeKeyCreation, 'g-')
    #plt.title('n-bit Key Creation Time')
    #plt.ylabel('time in seconds')
    #plt.xlabel('key length')



    plt.subplot(2, 1, 2)
    ax = plt.subplot(111)
    plt.title('Encryption Time')
    plt.ylabel('time in seconds')
    plt.xlabel('Message Length')
    for i,val in enumerate(runTimeEncryption):
        ax.plot(nBytes_to_test[0:len(val)],val, label="Key=%d"%(nKeys_to_test[i]))
    #chartBox = ax.get_position()
    #ax.set_position([chartBox.x0, chartBox.y0, chartBox.width * 0.6, chartBox.height])
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=5, mode="expand", borderaxespad=0.)

    #plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
    plt.show()


main()