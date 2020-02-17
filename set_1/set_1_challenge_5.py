def xor_repeated_key(byte_input, byte_key):
    gen_key = repeat_key(byte_key)
    return bytes([byte ^ next(gen_key) for byte in byte_input])


def repeat_key(byte_key):
    while True:
        for byte in byte_key:
            yield byte


def main():
    input_string = bytes(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")

    print(xor_repeated_key(input_string, list(map(lambda x: ord(x), 'ICE'))).hex())


if __name__ == '__main__':
    main()
