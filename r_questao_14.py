nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1+nota2)/2

if (media>=9.0 and media<=10.0):
    print('{} pontos, média de aproveitamento: A.'.format(media))
else:
    if (media>=7.5 and media<=9.0):
        print('{} pontos, média de aproveitamento: B.'.format(media))
    else:
        if (media>=6.0 and media<=7.5):
            print('{} pontos, média de aproveitamento: C.'.format(media))
        else:
            if (media>=4.0 and media<=6.0):
                print('{} pontos, média de aproveitamento: D.'.format(media))
            else:
                print('{} pontos, média de aproveitamento: E.'.format(media))
