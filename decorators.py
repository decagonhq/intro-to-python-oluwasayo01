def decorate(func):
    def wrapper(plaintext):
        print('='*len(func(plaintext)))
        print(func(plaintext))
        print('='*len(func(plaintext)))

    return wrapper

def encrypt(func):
    def wrapper(plaintext, encryption_key):
        # plaintext = len(func(plaintext))
        string = encryption_key.upper()
        k = len(string)
        j = 0
        ciphertext = ''
        for i in range(len(func(plaintext, encryption_key))):
            if string[i%k].isdigit():
                ciphertext += plaintext[i]
                continue

            key = (i - j) % k
            if plaintext[i].isupper():
                capital = ((ord(plaintext[i]) - ord('A')*2)+ ord(string[key])) % 26
                c = chr(capital + ord('A'))
                ciphertext += c
                # print(ciphertext)
            if plaintext[i].islower():
                small = ((ord(plaintext[i]) - ord('a'))+ ord(string[key]) - ord('A')) % 26
                c = chr(small + ord('a'))
                ciphertext += c
                # print(ciphertext)
            if not plaintext[i].isalpha():
                ciphertext += plaintext[i]
                j += 1
        return ciphertext
    return wrapper



@encrypt
def hello(plaintext, encryption_key):
    return plaintext

@decorate
def text(input_text):
    return 20*input_text

print(hello("Hello World!", 'abc'))
print(text('500'))