def retorna_p_inteira(string_num):
    string = ""
    for i in range(len(string_num)):
        if string_num[i] != ',' and string_num[i] != '.':
            string += string_num[i]
        else:
            break
    return int(string)

def converte_int_bin(inteiro):
    '''retorna o binário na forma de string'''
    str_bin = ""
    if inteiro == 0:
        str_bin += "0"
        return str_bin

    resto = []
    div = inteiro
    while div != 0:
        r = div % 2
        div = div // 2
        resto.append(r)

    for i in range(len(resto) - 1, -1, -1):
        str_bin += str(resto[i])
        
    return str_bin

def converte_float_bin(numero):
    string = ""
    if numero == 0:
        string += '0'
        return string

    while numero != 0:
        numero = numero * 2
        if numero >= 1:
            V = 1
        else:
            V = 0
        numero = numero - V
        string += str(V)
    return string

def corrige_virgula(num):
    string = ""
    for i in range(len(num)):
        if num[i] != ",":
            string += num[i]
        else:
            string += "."
    return string

num = input("Digite o número com vírgula a ser transformado em binário: ")

# pego a parte inteira do número
pint = retorna_p_inteira(num)
print("parte inteira =", pint)

# converto ela pra binário
bina = converte_int_bin(pint)

# pego a parte decimal que sobrou
aux = float(corrige_virgula(num))
decimal = aux - pint

# converto pra binário
dec_bin = converte_float_bin(decimal)

# junto as duas
resultado = bina + ',' + dec_bin
print(num, "em binário é", resultado)
