def pkcs7_pad(block_size, message):
    bytes_to_pad = block_size - (len(message) % block_size)
    return message + bytes([bytes_to_pad for _ in range(bytes_to_pad)])


def main():
    data = b"YELLOW SUBMARINE"
    print(pkcs7_pad(20, data))


if __name__ == '__main__':
    main()
