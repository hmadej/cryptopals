def xor_repeat_key(string_input, string_key):
    byte_input = list(map(lambda c: ord(c), string_input))
    byte_key = list(map(lambda c: ord(c), string_key))
    gen_key = repeat_key(byte_key)
    return bytes([byte ^ next(gen_key) for byte in byte_input])


def repeat_key(byte_key):
    while True:
        for byte in byte_key:
            yield byte


def main():
    input_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    print(xor_repeat_key(input_string, 'ICE').hex())


if __name__ == '__main__':
    main()
