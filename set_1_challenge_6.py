from set_1_challenge_3 import xor_key
from set_1_challenge_5 import xor_repeated_key
from collections import Counter
from base64 import b64decode


def hamming_distance(string_1, string_2):
    return sum([bin(a ^ b).count('1') for a, b in zip(string_1, string_2)])


# take the first KEYSIZE byte from string, and second KEYSIZE byte from string take the hamming distance of these two
# strings and normalize by dividing by KEYSIZE, continue this for the length of the string to get the average
# { keysize: n
#   average_distance:
# }

def average_keysize_distance(byte_string):
    average_distances = []
    for key_size in range(2, 41):
        distance_sum = 0
        intervals = len(byte_string) // key_size
        for i in range(intervals):
            distance_sum += hamming_distance(byte_string[key_size * i:(key_size) * (i + 1)],
                                             byte_string[key_size * (i + 1):key_size * (i + 2)])
        average_distances.append(
            {
                'keysize': key_size,
                'average distance': distance_sum / (intervals * key_size)
            }
        )
    return sorted(average_distances, key=lambda x: x['average distance'])


def transpose(list, key_size):
    blocks = []
    for i in range(key_size):
        block = b''
        for j in range(i, len(list), key_size):
            block += bytes([list[j]])
        blocks.append(block)
    return blocks


character_frequency = {
    'e': .127, 't': .097, 'i': .075, 'a': .073, 'o': .068, 'n': .067, 's': .067, 'r': .064, 'h': .049,
    'c': .045, 'l': .040, 'd': .031, 'p': .030, 'y': .027, 'u': .024, 'm': .024, 'f': .021, 'b': .017,
    'g': .016, 'w': .013, 'v': .008, 'k': .008, 'x': .005, 'q': .002, 'z': .001, 'j': .001, ' ': .13,
    '\n': .13
}


def scoring(frequency_list):
    score = 0
    for char, count in frequency_list:
        if chr(char) in character_frequency:
            score += character_frequency[chr(char)] * count
    return score


def main():
    with open('encrypted.txt', 'r') as f:
        cipher_text = b64decode(f.read())

    key_length_guess = average_keysize_distance(cipher_text)[0]
    transposed_blocks = transpose(cipher_text, key_length_guess['keysize'])
    key = []
    for block in transposed_blocks:
        scores = []
        for c in range(255):
            deciphered_text = xor_key(block, c)
            scores.append((scoring(Counter(deciphered_text).most_common()), c))
        key.append(sorted(scores, key=lambda x: x[0], reverse=True)[0][1])

    print(key_length_guess, xor_repeated_key(cipher_text, key))



if __name__ == '__main__':
    main()
