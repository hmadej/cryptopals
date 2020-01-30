from set_1_challenge_3 import histogram_scoring


def main():
    with open('strings.txt', 'r') as f:
        hex_inputs = f.readlines()

    hex_inputs = list(map(lambda x: bytes.fromhex(x), hex_inputs))
    print(histogram_scoring(hex_inputs)[0])


if __name__ == '__main__':
    main()
