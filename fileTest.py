from RSA import RSA
from datetime import datetime

rsa = RSA()
#rsa.RSA_Algorithm()
rsa.getPublicKeyFromFile("./keys/publicKeyFile.txt")
rsa.getPrivateKeyFromFile("./keys/privateKeyFile.txt")



eRts = datetime.now() # encryption run time start
rsa.encryptTextFile("./data/bigtext.txt", "./data/bigtextencrypted.txt")
eRte = datetime.now() # encryption run time end
eMsgT = (eRte-eRts).total_seconds() #encrypt message time

dRts = datetime.now() # decryption run time start
rsa.decryptTextFile("./data/bigtextencrypted.txt", "./data/bigtextdecrypted.txt")
dRte = datetime.now() # decryption run time end
dMsgT = (dRte-dRts).total_seconds() #encrypt message time

print("The encryption time is:", eMsgT)
print("The decryption time is:", dMsgT)