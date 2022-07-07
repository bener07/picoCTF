# importamento de string, para ter ascii_lowercase
import string
# definição das variavéis 
LOWERCASE_OFFSET = ord("a") # determina o OFFSET que será igual a 97 para ser utilizado na função shift
ALPHABET = string.ascii_lowercase[:16] # definir ĺista com abcedário de 16 letras
flag = 'kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm' # definição da flag


# na função b16_encode o caracter recebido, o seu valor binário é dividido em 2 separando assim os primeiros 4 btis dos 4 ultimos bits
def decoder(cipher):
        first = ALPHABET.index(cipher[0]) # pega no primeiro caracter e calcula o seu index em ALPHABET
        second = ALPHABET.index(cipher[1]) # pega no segundo caracter e calcula o seu index em ALPHABET
        res = "{0:04b}".format(first) # pega no primeiro index e transforma o seu valor decimal em binário
        byte = res + "{0:04b}".format(second) # pega no valor binário do index do segundo caracter e adiciona ao valor binário
                                              # do index do primeiro caracter
        return chr(int(byte, 2)) # utiliza a junção das strings dos 2 valores binários e calcula o seu valor decimal 
                                 # calculando assim a sua posição na tabela ascii
                                 # ex ('gb'): 
                                 #      first = 6
                                 #      second = 1
                                 #      valor binário:
                                 #              first = '0110'
                                 #              second = '0001'
                                 #              byte = '01100001'
                                 #      int(byte, 2) = 97
                                 #      chr(97) = 'a'
                                 # 'gb' = 'a'


def deshift(c, k):
        index1 = ALPHABET.index(c) # pega no index do caracter para trocar
        index2 = ALPHABET.index(k) # pega no index da chave usada para trocar o caracter
        character_offset = ALPHABET[index1 - index2] # pega no caracter trocado e subtrai o seu index pelo index da chave
                                                     # e obtém o caracter original antes de ser trocado com o index da chave
                                                     # Ex: 'd' com chave 'c', o index de 'd' = 3 o index de 'c' = 2 
                                                     # 2 - 3 = 2 o caracter 'd' fica um 'b' caracter original antes do shift
        return chr(ALPHABET.index(character_offset)+97) # Aqui devolve o ascii do index do caracter character_offset + 97
                                                        # + 97 pois foi feito a subtracão de ord(c) com 97 para obter o valor dentro 
                                                        # de ALPHABET. Nesta função o index de 'd' = 3 e quando se adiciona 97
                                                        # fica 100 e o chr(100) ou seja o valor ascii na tabela ascii com index 100
                                                        # é o 'd'.
                # Atenção! Esta função ajudou-me num melhor entendimento da função shift, mas não é obrigatória pois a própria 
                # função shift troca o valor para o original, basta ter a chave certa.

# definição das variáveis dentro destes loops
enc = ''# encoding
res = '' # resposta

for k in ALPHABET: # vamos fazer um bruteforce com todas as chaves possiveis dentro de ALPHABET
        n = 0 # n para o loop n que vai passar de 2 em dois
        for c in flag: # vai-se trocar todos os caracteres dentro da string flag para o seu valor original com a chave k
                enc += "{}".format(deshift(c, k))
        while(n<len(flag)): # vai-se fazer o decoding de flag e como temos de fazer de dois em dois usamos um while loop
                            # assim quando pegarmos em dois caracteres, asgr esses caracteres não se vão repetir
                            # sem loop ('bghj'):
                            #           'bg'
                            #           'gh'
                            #           'hj'
                            # com loop:
                            #           'bg'
                            #           'hj'
                res += decoder((enc[n]+enc[n+1]))
                n += 2 # adiciona mais 2 para passar impedir o efeito descrito em cima

        print(f"picoCTF{ {res} }") # faz o print de todas as flags possiveis com uma especifica chave
        res = '' # reseta res para no próximo ciclo não aparecer a flag atual mais a anterior
        enc = '' # reseta res para no próximo ciclo os caracteres trocados não incluirem valores anteriores