import random

def generateSequence():
    return random.sample(range(100), 26)

def encrypt(text, k, sequence):
    result = []

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            index = (ord(char) + k - 65) % 26
            result.append(sequence[index])
        else:
            index = (ord(char) + k - 97) % 26
            result.append(sequence[index])

    return result


def decrypt(text, k, sequence):
    result = ""

    for i in range(len(text)):
        char = text[i]

        index = sequence.index(char)
        result += chr((index - k) % 26 + 97)

    return result

if __name__ == '__main__':
    sequence = generateSequence()
    print(sequence)
    encrypted = encrypt('abcd', 100, sequence)
    print(f'Encrypted text: {encrypted}')

    decrypted = decrypt(encrypted, 100, sequence)
    print(f'Decrypted text: {decrypted}')
