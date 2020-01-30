from collections import Counter

character_frequency = {
    'e': .127, 't': .097, 'i': .075, 'a': .073, 'o': .068, 'n': .067, 's': .067, 'r': .064, 'h': .049,
    'c': .045, 'l': .040, 'd': .031, 'p': .030, 'y': .027, 'u': .024, 'm': .024, 'f': .021, 'b': .017,
    'g': .016, 'w': .013, 'v': .008, 'k': .008, 'x': .005, 'q': .002, 'z': .001, 'j': .001, ' ': .13
}


def scoring(frequency_list):
    score = 0
    for char, count in frequency_list:
        if char in character_frequency:
            score += character_frequency[char] * count
        else:
            score -= 0.01
    return score


def xor_key(input_bytes, key):
    return [byte ^ key for byte in input_bytes]


def histogram_scoring(inputs):
    key = []
    for input_byte in inputs:
        scores = []
        for n in range(128):
            decoded = ''.join(map(lambda c: chr(c), xor_key(input_byte, n)))
            scores.append((chr(n), scoring(Counter(decoded).most_common()), bytes(xor_key(input_byte, n))))

        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        for score in sorted_scores[:4]:
            key.append(score)

    return sorted(key, key=lambda x: x[1], reverse=True)


def main():
    input_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    hex_string = bytes.fromhex(input_string)
    print(bytes(xor_key(hex_string, ord(histogram_scoring([hex_string])[0][0]))))


if __name__ == '__main__':
    main()
