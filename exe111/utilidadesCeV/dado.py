def leiaDinheiro(msg):
    val = False
    while not val:
        ent = str(input(msg)).replace(',','.')
        if ent.isalpha() or ent.strip() == '':
            print(f'\033[0;31m{ent} e um preco invalido!\033[m')
        else:
            val = True
            return float(ent)