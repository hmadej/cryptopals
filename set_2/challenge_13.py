import re

from challenge_11 import encrypt_ECB, generate_key, decrypt_ECB


def profile_for(email_string):
    if invalid_email(email_string):
        return ("email={0}&uid={1}&role={2}".format(email_string, 10, 'user')).encode('utf-8')
    else:
        print("bad email string! -> {}".format(email_string))
    return None


def invalid_email(email_string):
    # email_pattern = "([a-zA-Z._0-9]*@([a-zA-Z0-9]*\.)*[a-zA-Z]+)"
    email_pattern_bad = "([&=]*)"
    email_regex = re.compile(email_pattern_bad)
    return email_regex.match(email_string)


def parse(input_string):
    pos, length, kv_store = 0, len(input_string), dict()
    key, value, remaining = pair(input_string)
    kv_store[key] = value
    while remaining:
        if remaining[0] == '&':
            key, value, remaining = pair(remaining[1:])
            kv_store[key] = value
        else:
            print("something bad happened, no & -> {}".format(remaining))
            remaining = remaining[1:]

    return kv_store


def pair(parsed_string):
    key, remaining = parse_key(parsed_string)
    if (not remaining) or remaining[0] != '=':
        print("something bad happened, no equals -> {}".format(remaining))
    remaining = remaining[1:]
    value, remaining = parse_value(remaining)
    return key, value, remaining


def parse_key(parsed_string):
    remaining = parsed_string
    key = ''
    while remaining and remaining[0] != '=':
        key += remaining[0]
        remaining = remaining[1:]
    return key, remaining


def parse_value(parsed_string):
    remaining = parsed_string
    val = ''
    while remaining and remaining[0] != '&':
        val += remaining[0]
        remaining = remaining[1:]
    return val, remaining


def main():
    cookie = "foo=bar&baz=qux&zap=zazzle"
    key = generate_key(16)
    profile_string = profile_for("cat@gmail.com")
    cipher_text = encrypt_ECB(key, profile_string)

    print(profile_string)
    for i in range(0, len(cipher_text), 16):
        print(cipher_text[i:i + 16])

    print("\n")
    fake_profile_string = profile_for("cat@gmail.admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b")
    fake_cipher_text = encrypt_ECB(key, fake_profile_string)

    for i in range(0, len(cipher_text), 16):
        print(fake_cipher_text[i:i + 16])

    print("\n")

    new_profile_cipher = cipher_text[0:32] + fake_cipher_text[16:32]
    print(new_profile_cipher)
    print(decrypt_ECB(key, new_profile_cipher))


if __name__ == '__main__':
    main()
