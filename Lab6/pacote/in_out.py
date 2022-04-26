def ler_numero():
    try:
       int(input('Insira um inteiro'))
    except:
        print('Não meteu um numero inteiro')   
        
def imprime_resultados(n,positivo,par):
    if positivo:
        positivo = 'positivo'
    else:
        positivo = 'negativo'
    if par:
        par = 'par'
    else:
        par = 'impar'
    print(f'O numero {n} é {positivo} e {par}')