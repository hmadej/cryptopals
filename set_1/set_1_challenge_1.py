b64_encoding_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


# b64_table = 'WXYZlabcd3fghijko12e456789ABCDEFGHIJKL+/MNOPQRSTUVmn0pqrstuvwxyz'


def b64_encode(table, input_bytes, padding_char='='):
    bits = ''.join(list(map(lambda byte: bin(byte)[2:].zfill(8), input_bytes)))
    rest = bits
    encoding_accumulator = ''

    while len(rest) >= 6:
        chunk, rest = rest[:6], rest[6:]
        index = int(chunk, 2)
        encoding_accumulator += table[index]

    if len(rest) == 4:
        rest += '00'
        encoding_accumulator += table[int(rest, 2)] + padding_char
    elif len(rest) == 2:
        rest += '0000'
        encoding_accumulator += table[int(rest, 2)] + padding_char * 2

    return encoding_accumulator


def b64_decode(table, input_string, padding_char='='):
    try:
        bits = ''.join(list(map(lambda char: bin(table.index(char))[2:].zfill(6), input_string.strip(padding_char))))
        rest = bits
        decoding_accumulator = []
        while len(rest) >= 8:
            chunk, rest = rest[:8], rest[8:]
            decoding_accumulator.append(int(chunk, 2))
        return bytes(decoding_accumulator)

    except ValueError as e:
        print("Not encoded using this table")
        print(e)


def fixed_xor(input_bytes_1, input_bytes_2):
    output = bytes([a ^ b for a, b in zip(input_bytes_1, input_bytes_2)])
    return output


def main():
    hex_bytes = bytearray(
        b'\x49\x27\x6d\x20\x6b\x69\x6c\x6c\x69\x6e\x67\x20\x79\x6f\x75\x72\x20\x62\x72\x61\x69\x6e\x20\x6c\x69\x6b\x65'
        b'\x20\x61\x20\x70\x6f\x69\x73\x6f\x6e\x6f\x75\x73\x20\x6d\x75\x73\x68\x72\x6f\x6f\x6d')

    print(hex_bytes)
    print(
        b64_encode(b64_encoding_table, hex_bytes) == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    print(fixed_xor(b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02\x4b\x53\x53\x50\x09\x18\x1c',
                    b'\x68\x69\x74\x20\x74\x68\x65\x20\x62\x75\x6c\x6c\x27\x73\x20\x65\x79\x65')
          .hex())
    print(b64_decode(b64_encoding_table, 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'))


if __name__ == '__main__':
    main()
