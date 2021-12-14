palavras = ('aprender', 'programar','realizar','continuar',
            'utilizar', 'estudar', 'praticar', 'trabalhar',
            'programador','trabalhar', 'futuro')

for p in palavras:
    print(f"\n na palavra {p.upper()} temos ", end ='' )
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')

