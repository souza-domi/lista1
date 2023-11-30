
#Dominique Rodrigues de Souza 
#DRE 121041452


def ehNumero (numero):
    '''Retorna True caso o numero seja positivo e real'''
    
    try: 
        float(numero)
    except ValueError:
        return False
    return True

#Questao 11

def calculadora ():
    '''Dados dois numeros inteiros e um real, calcula e mostra:
    a)o produto do dobro do primeiro com metade do segundo
    b)a soma do triplo do primeiro com o terceiro
    c)o terceiro elevado ao cubo
    '''

    #Condicoes
    x = input ('Insira um numero inteiro: ')
    while x.isdigit() == False:
        x = input ('Tente novamente. Insira um numero inteiro: ')
    
    y = input ('Insira outro numero inteiro: ')
    while y.isdigit() == False:
        y = input ('Tente novamente. Insira outro numero inteiro: ')
    
    z = input ('Insira um numero real: ')
    while ehNumero(z) == False:
        z = input ('Tente novamente. Insira um numero real: ')
     
    #calculos

    a = (2 * int(x)) * (int(y)/2)
    b = 3 * int(x) + float(z)
    c = pow(float(z) , 3)

    #Respostas

    print (str.format('a) {}',a))
    print (str.format('b) {}',b))
    print (str.format('c) {}',c))

#Questao 12

def pesoIdeal ():
    '''Dada a altura retorna o peso ideal 
    float -> float'''
    
    altura = input('Insira sua altura em metro: ')
    while ehNumero(altura) == False:
        altura = input('Tente novamente. Insira sua altura em metro: ')
    peso = round((72.2 * float(altura)) - 58,1)
    return str.format('{} kg',peso) 

#Questao 13

def pesoIdealGenero():
    '''Pede genero e altura e retorna o peso ideal'''

    g = input('Insira H para homem e M para mulher: ')
    while g != 'M' and g != 'm' and g != 'H' and g != 'h':
            g = input('Tente novamente. Insira H para homem e M para mulher: ')
    
    altura = input('Insira sua altura em metro: ')
    while ehNumero(altura) == False:
        altura = input('Tente novamente. Insira sua altura em metro: ')
    
    if g == 'H' or g == 'h':
        peso = round((72.2 * float(altura)) - 58,1)
        return str.format('{} kg',peso) 
    else:
       peso = round((62.1 * float(altura)) - 44.7)
       return str.format('{} kg',peso)
    
#Questao 14

def multa():
    '''Dado o peso de peixes, retorna o peso excedente e o valor da multa a ser paga.'''

    peso = input('Insira o peso de peixe em kg: ')

    while ehNumero(peso) == False:
        peso = input('Tente novamente. Insira o peso de peixe em kg: ')
    
    if float(peso) > 50:
        excesso = round(float(peso) - 50, 2)
        multa = round(4 * excesso, 
                      2)
        return  str.format('Voce excedeu em {} kg. A multa a ser paga eh de R$ {}', excesso, multa )
    else:
        return str.format('Peso dentro do padrao estabelecido. Nao ha multas a pagar.')

