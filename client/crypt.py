from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def AESencrypt(text):
    aeskey = Random.new().read(32)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(aeskey, AES.MODE_CFB, iv)
    return (aeskey, iv, cipher.encrypt(text))

def AESdecrypt(aeskey, iv, cipherText):
    cipher = AES.new(aeskey, AES.MODE_CFB, iv)
    return cipher.decrypt(cipherText)
    
def loadKey(keyFileName):
    keyfile = open(keyFileName, "r")
    key = keyfile.read()
    keyfile.close()
    return RSA.importKey(key)

def Encrypt(text):
    # Encrypt text using AES
    (aeskey, iv, msg) = AESencrypt(text)
    
    # Encrypt AES key using RSA
    cipher = PKCS1_OAEP.new(loadKey("public.key"))
    aesKeyCipherText = cipher.encrypt(aeskey)
    
    return (aesKeyCipherText, iv, msg)

def Decrypt(aesCipherText, iv, msg):
    # Decrypt AES key using RSA
    cipher = PKCS1_OAEP.new(loadKey("private.key"))
    aesKey = cipher.decrypt(aesCipherText)
    
    # Decrypt text using AES
    return AESdecrypt(aesKey, iv, msg)
