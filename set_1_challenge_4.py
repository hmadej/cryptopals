from set_1_challenge_3 import score, xor_key
from collections import Counter


def main():
    with open('strings.txt', 'r') as f:
        hex_inputs = f.readlines()

    hex_inputs = list(map(lambda x: bytes.fromhex(x), hex_inputs))
    scores = []
    for hex_input in hex_inputs:
        for n in range(32, 127):
            decoded = ''.join(map(lambda c: chr(c), xor_key(hex_input, n)))
            scores.append((chr(n), score(Counter(decoded).most_common()), hex_input))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for i in range(5):
        print(''.join(map(lambda c: chr(c), xor_key(sorted_scores[i][2], ord(sorted_scores[i][0])))), sorted_scores[i])


if __name__ == '__main__':
    main()
