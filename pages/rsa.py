from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class rsaClass:
    keySize = 1024
    publicExponent = 65537

    privateKey = rsa.generate_private_key(public_exponent = publicExponent, key_size = keySize)
    publicKey = privateKey.public_key()
    message = ""

    encrypted = publicKey.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    decrypted = privateKey.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))