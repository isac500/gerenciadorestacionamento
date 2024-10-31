from math import ceil
from datetime import date
from os import system
def inicio():
    dia = date.today().day
    mes = date.today().month
    if dia < 10 and mes < 10:
        print('*' * 28, '                \033[1m\033[7;38;40mData: {}{}/{}{}/{}\033[m\033[m'.format(0, dia, 0, mes,
                                                                                                    date.today().year))
    elif dia < 10 and mes > 9:
        print('*' * 28, '  \033[1m\033[7;38;40mData: {}{}/{}/{}\033[m\033[m'.format(0, dia, mes, date.today().year))
    elif dia > 9 and mes < 10:
        print('*' * 28, '  \033[1m\033[7;38;40mData: {}/{}{}/{}\033[m\033[m'.format(dia, 0, mes, date.today().year))
    print('\033[1m\033[4;36mEstacionamento "Aí DentU"\033[m\033[m  ')
    print('***********\033[1;34m MENU\033[m ***********')
    print(
        '\033[1;32mEntrada [1]\033[m - \033[1;31mSaída [2]\033[m \033[1;37m \nPátio [3]\033[m - \033[1;33mFechar Sistema [0]\033[m')
    print('*********** \033[1;34mPREÇO\033[m ********** \n\033[1;35m5,00 R$\033[m até 1 hora.')
    print('Caso passe do horário, será cobrado mais 1 hora.')
    print('\033[1mNÃO HÁ TOLERÂNCIA!\033[m')
    print('*' * 60)
dia = date.today().day
mes = date.today().month
if dia < 10 and mes < 10:
    print('*' * 28, '                \033[1m\033[7;38;40mData: {}{}/{}{}/{}\033[m\033[m'.format(0, dia, 0, mes, date.today().year))
elif dia < 10 and mes > 9:
    print('*' * 28, '  \033[1m\033[7;38;40mData: {}{}/{}/{}\033[m\033[m'.format(0, dia, mes, date.today().year))
elif dia > 9 and mes < 10:
    print('*' * 28, '  \033[1m\033[7;38;40mData: {}/{}{}/{}\033[m\033[m'.format(dia, 0, mes, date.today().year))
print('\033[1m\033[4;36mEstacionamento "Aí DentU"\033[m\033[m  *')
print('***********\033[1;34m MENU\033[m ***********')
print('\033[1;32mEntrada [1]\033[m - \033[1;31mSaída [2]\033[m \033[1;37m \nPátio [3]\033[m - \033[1;33mFechar Sistema [0]\033[m')
print('*********** \033[1;34mPREÇO\033[m ********** \n\033[1;35m5,00 R$\033[m até 1 hora.')
print('Caso passe do horário, será cobrado mais 1 hora.')
print('\033[1mNÃO HÁ TOLERÂNCIA!\033[m')
print('*' * 60)
fechar = '\033[1;34m'
lista1 = []
cont = '1'
patio = 0
while cont != '0':
    print('Veículos no pátio: {}'.format(patio))
    cont = (input('Digite aqui (\033[1;32mEntrar[1]\033[m - \033[1;31mSaída[2]\033[m - \033[1;37mPátio[3]\033[m - \033[1;33mFechar[0]\033[m): '))
    if cont == '1':
        placa = str(input('Placa: ')).upper().strip()
        if len(placa) != 7:
            system('clear')
            inicio()
            print('Formato de placa incompatível!')
            print('Formatos compatíveis: ABC1234 - ABC1D23')
            print('*' * 60)

        else:
            if placa in lista1:
                system('clear')
                inicio()
                print('Este veículo já está no pátio...')
                print('*' * 60)
            else:
                lista1.append(placa)
                patio = patio + 1
                system('clear')
                inicio()
    elif cont == '2':
        if patio > 0:
            sai = str(input('Digite a placa do veículo que irá saí: ')).upper().strip()
            if sai in lista1:
                horas = float(input('Quantidade de horas que o veículo ficou no pátio (formato: 00.00): '))
                horas = ceil(horas)
                preco = horas * 5
                lista1.remove(sai)
                patio = patio - 1
                system('clear')
                inicio()
                print('Saída: \033[1;36m{}\033[m - Total a ser pago: \033[1;36m{:.2f} reais\033[m.'.format(sai, preco))


            else:
                system('clear')
                inicio()
                print('Veículo não se encontra no pátio.')

        else:
            system('clear')
            inicio()
            print('Pátio Vazio....')

    elif cont == '3':
        if patio > 0:
            system('clear')
            inicio()
            print('Veículos no pátio: \n\033[1;36m{}\033[m'.format(lista1))

        else:
            system('clear')
            inicio()
            print('Pátio Vazio....')

    #elif cont >= 4:
     #   print('Digito Inválido...')
      #  print('*' * 60)
    elif cont == '0':
        print(fechar + 'Sistema Encerrado!\033[m')
        print('*' * 60)
    else:
        system('clear')
        inicio()
        print('Dígito Inválido....')

