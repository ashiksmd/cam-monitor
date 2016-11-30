from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
rsakey = RSA.generate(1024, random_generator)

privateKey = rsakey.exportKey()
publicKey = rsakey.publickey().exportKey()

with open("private.key", "w") as privateKeyFile:
    privateKeyFile.write(privateKey)

with open("public.key", "w") as publicKeyFile:
    publicKeyFile.write(publicKey)
