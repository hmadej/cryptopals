from collections import Counter

frequency_dict = {
    'e': .127, 't': .097, 'i': .075, 'a': .073, 'o': .068, 'n': .067, 's': .067, 'r': .064, 'h': .049,
    'c': .045, 'l': .040, 'd': .031, 'p': .030, 'y': .027, 'u': .024, 'm': .024, 'f': .021, 'b': .017,
    'g': .016, 'w': .013, 'v': .008, 'k': .008, 'x': .005, 'q': .002, 'z': .001, 'j': .001
}


def score(frequency_list):
    current_score = 0
    for char, count in frequency_list:
        if char in frequency_dict:
            current_score += frequency_dict[char] * count
        elif char == ' ':
            current_score += 0.3 * count
    return current_score


def xor_key(input_bytes, key):
    return [byte ^ key for byte in input_bytes]


def main():
    input_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    hex_string = bytes.fromhex(input_string)
    scores = []
    for n in range(32, 127):
        decoded = ''.join(map(lambda c: chr(c), xor_key(hex_string, n)))
        scores.append((chr(n), score(Counter(decoded).most_common())))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for i in range(5):
        print(''.join(map(lambda c: chr(c), xor_key(hex_string, ord(sorted_scores[i][0])))), sorted_scores[i])



if __name__ == '__main__':
    main()
