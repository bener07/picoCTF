import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
                binary = "{0:08b}".format(ord(c)) # Convert o texto da vari  vel do loop c em bin  rio Ex: 'a' == 01100001
                enc += ALPHABET[int(binary[4:], 2)] # para caracter 'a' faz os primeiros 4 bits e devolve o seu valor decimal que    6
                enc += ALPHABET[int(binary[:4], 2)] # para caracter 'a' faz os ultimos 4 bits e devolve o seu valor decimal que    1
                print(enc)
        return enc


def shift(c, k):
        t1 = ord(c) - 97 # subtrai o valor do caracter com o valor da primeira letra de ALPHABET ou seja o index do caracter
                         # 'a' == 0 ALPHABET[0] == 'a'
                         #
        t2 = ord(k) - 97 # subtrai o valor do caracter com o valor da primeira letra de ALPHABET e utiliza t2 como chave
        return ALPHABET[(t1 + t2) % len(ALPHABET)] # (t1+t2) adiciona t1(index do caracter dentro de ALPHABET)
                                                   # e t2 (index do caracter chave dentro de ALPHABET)
                                                   # ex caracter 'a' com chave 'c' o caracter 'a' transforma-se em 'c'
 


flag = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
key = "b" # a assertation verifica se a chave existe
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
print(b16)
for i, c in enumerate(b16):
        enc += shift(c, key)
print(enc)
