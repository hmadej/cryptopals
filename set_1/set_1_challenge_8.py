# detect AES in ECB mode

# ECB mode means pieces of the block are encrypted by pieces of the key only, no IV, no forward feeding
# So if piece is the same or the same piece occurs frequently it may indicate ECB.


def split_chunks(cipher_text, block_size):
    return [cipher_text[i:i + block_size] for i in range(0, len(cipher_text), block_size)]


def count_repetitions(chunks):
    return len(chunks) - len(set(chunks))


def main():
    with open('ecbciphertext.txt', 'r') as f:
        cipher_text = [bytes.fromhex(line.strip()) for line in f.readlines()]
        repetitions = list(map(count_repetitions, [split_chunks(cipher, 16) for cipher in cipher_text]))
        print(cipher_text[repetitions.index(max(repetitions))])


if __name__ == '__main__':
    main()
