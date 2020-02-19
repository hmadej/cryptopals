from base64 import b64decode
from functools import reduce
from math import gcd

from challenge_11 import encrypt_ECB, generate_key, is_ECB_mode


def main():
    unknown_string = b64decode(
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    key = generate_key(16)

    # determining the block size of the cipher and the block mode.
    max_block_size = 64
    ciphers = [encrypt_ECB(key, b'a' * 4 * i + unknown_string) for i in range(1, max_block_size + 1)]
    cipher_length = len(ciphers[0])
    block_size = reduce(min, map(lambda cipher: gcd(cipher_length, len(cipher)), ciphers))

    print("Cipher is ECB Mode: {}".format(is_ECB_mode(ciphers[-1], block_size)))

    # decrypting the unknown string, with unknown key.
    one_byte_short = b'a' * (block_size - 1)

    short_ciphers = dict()
    for i in range(0, 127):
        key_value = encrypt_ECB(key, one_byte_short + bytes([i]))
        short_ciphers[key_value] = bytes([i])

    missing_bytes = [encrypt_ECB(key, one_byte_short + unknown_string[j:])[:16] for j in range(len(unknown_string))]

    decoded_string = b''.join(map(lambda x: short_ciphers[x], missing_bytes))
    print(decoded_string)


if __name__ == '__main__':
    main()
