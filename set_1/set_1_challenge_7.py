from base64 import b64decode

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

cipher = Cipher(algorithms.AES(bytes(b'YELLOW SUBMARINE')), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()
with open('ciphertext.txt', 'r') as f:
    ct = b64decode(f.read())
    print(decryptor.update(ct) + decryptor.finalize())
