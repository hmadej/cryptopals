import random
from functools import reduce

from challenge_10 import encrypt_CBC
from challenge_9 import pkcs7_pad
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# ECB/CBC Detection oracle


def encrypt_ECB(key, plaintext):
    cipher = Cipher(algorithms.AES(bytes(key)), modes.ECB(), backend=default_backend())
    en = cipher.encryptor()
    cipher_text = []
    for i in range(0, len(plaintext) - 1, 16):
        block = plaintext[i:i + 16]
        if len(block) != 16:
            block = pkcs7_pad(16, block)
        cipher_text.append(en.update(block))
    en.finalize()
    return reduce(lambda a, b: a + b, cipher_text)


def encryption_oracle(plaintext):
    AES_key = generate_key(16)
    prefix_bytes = generate_key(random.randint(5, 10))
    suffix_bytes = generate_key(random.randint(5, 10))
    plaintext = prefix_bytes + plaintext + suffix_bytes
    if random.getrandbits(1) == 0:
        cipher_text = encrypt_ECB(AES_key, plaintext)
    else:
        iv = generate_key(16)
        cipher_text = encrypt_CBC(AES_key, iv, plaintext)
    return cipher_text


def generate_key(num):
    # num is the number of bytes for the key as an int
    random.seed()
    return bytes([random.getrandbits(8) for _ in range(num)])


def is_ECB_mode(cipher_text, block_size):
    size = block_size
    blocks = set()
    for i in range(0, len(cipher_text), size):
        blocks.add(cipher_text[i:i + size])

    return not len(blocks) == len(cipher_text) // size


def main():
    for _ in range(100):
        print(is_ECB_mode(encryption_oracle(b'a' * 16 * 4), 16))


if __name__ == '__main__':
    main()
