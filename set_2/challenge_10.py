from base64 import b64decode
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from challenge_9 import pkcs7_pad
from functools import reduce


def encrypt_CBC(key, iv, text):
    # key, iv, text are byte strings
    cipher = Cipher(algorithms.AES(bytes(key)), modes.ECB(), backend=default_backend())
    en = cipher.encryptor()
    block, rest = text[:16], text[16:]
    cipher_text = []
    while len(block) != 0:
        if len(block) != 16:
            block = pkcs7_pad(16, block)
        cipher_text.append(encrypt_block(en, iv, block))

        iv = cipher_text[-1]
        block, rest = rest[:16], rest[16:]

    en.finalize()
    return reduce(lambda a,b : a+b, cipher_text)

def decrypt_CBC(key, iv, text):
    # key, iv, text are byte strings
    cipher = Cipher(algorithms.AES(bytes(key)), modes.ECB(), backend=default_backend())
    de = cipher.decryptor()
    block, rest = text[:16], text[16:]
    plain_text = []
    while len(block) != 0:
        plain_text.append(bytes(decrypt_block(de, iv, block)))
        iv = block
        block, rest = rest[:16], rest[16:]

    de.finalize()
    return reduce(lambda a,b : a+b, plain_text)


def encrypt_block(encryptor, iv, plaintext):
    block = [(a ^ b) for a,b in zip(iv, plaintext)]
    cipher_text = encryptor.update(bytes(block))
    return cipher_text


def decrypt_block(decryptor, iv, ciphertext):
    plaintext = decryptor.update(ciphertext)
    plaintext = [(a ^ b) for a,b in zip(iv, plaintext)]
    return plaintext


def main():
    iv = b'\x00' * 16
    key = b"YELLOW SUBMARINE"
    plain_text = b"hello my name is henry, how are you"
    cipher_text = encrypt_CBC(key, iv, plain_text)
    y = decrypt_CBC(key, iv, cipher_text)
    print(y)


if __name__ == '__main__':
    main()