# QUESTÃO 2 de 4 (AULA 4) 
print('Bem-vindo a Sorveteria da Nataly Rossini')
print('------------------------------------------------Cardápio -----------------------------------------------')
print('| Código |        Descrição        |    Tamanho P (500ml) |   Tamanho M (1000ml) |  Tamanho G (1000ml) |')
print('|   TR   |    Sabores Tradicionais |       R$ 6,00        |         R$ 10,00     |       R$ 18,00      |')
print('|   ES   |    Sabores Especiais    |       R$ 7,00)       |         R$ 12,00     |       R$ 21,00      |')
print('|   PR   |    Sabores Premium      |       R$ 8,00        |         R$ 14,00     |       R$ 24,00      |')
print('--------------------------------------------------------------------------------------------------------')


acumulador = 0  #Necessário colocar este valor inicial na variável, pois iniciará com 0.
while True:
  tamanho_pote = input('Entre com o TAMANHO do pote desejado (P/M/G): ')
  tamanho_pote = tamanho_pote.upper()  #Este comando faz com que a string minúscula, caso aplicada, transforme-se em maíuscula.


  if tamanho_pote != 'P' and tamanho_pote != 'M' and tamanho_pote != 'G': #Condição atribuída a escolha do tamanho do pote de sorvete pelo usuário.
    print ('!!!!!!! TAMANHO OU CÓDIGOS INVÁLIDOS !!!!!')
    continue #Se o usuário digitar algo inválido, volta para o começo do while relacionado ao tamanho do pote.


  codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')
  codigo = codigo.upper() #Este comando faz com que a string minúscula, caso aplicada, transforme-se em maíuscula.
  if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
    print('!!!!!!! TAMANHO OU CÓDIGOS INVÁLIDOS !!!!!')
    continue #Se o usuário digitar algo inválido, volta para o começo do while.


  if codigo == 'TR' and tamanho_pote == 'P':
    print('Voce escolheu um sorvete TRADICIONAL P de R$6,00')
    print('-------------------------------------------------')
    acumulador = acumulador + 6 #Sempre desta maneira soma-se os valores conforme o pedido. É somado o valor do acumulador mais o valor 6


  elif codigo == 'TR' and tamanho_pote == 'M':
    print('Voce escolheu um sorvete TRADICIONAL M de R$10,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 10 #É somado o valor do acumulador mais o valor 10


  elif codigo == 'TR' and tamanho_pote == 'G':
    print('Voce escolheu um sorvete TRADICIONAL G de R$18,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 18 #É somado o valor do acumulador mais o valor 18


  elif codigo == 'ES' and tamanho_pote == 'P':
    print('Voce escolheu um sorvete ESPECIAL P de R$7,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 7 #É somado o valor do acumulador mais o valor 7


  elif codigo == 'ES' and tamanho_pote == 'M':
    print('Voce escolheu um sorvete ESPECIAL M de R$12,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 12 #É somado o valor do acumulador mais o valor 12


  elif codigo == 'ES' and tamanho_pote == 'G':
    print('Voce escolheu um sorvete ESPECIAL G de R$21,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 21 #É somado o valor do acumulador mais o valor 21


  elif codigo == 'PR' and tamanho_pote == 'P':
    print('Voce escolheu um sorvete PREMIUM P de R$8,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 8 #É somado o valor do acumulador mais o valor 8


  elif codigo == 'PR' and tamanho_pote == 'M':
    print('Voce escolheu um sorvete PREMIUM M de R$12,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 12 #É somado o valor do acumulador mais o valor 12


  elif codigo == 'PR' and tamanho_pote == 'G':
    print('Voce escolheu um sorvete PREMIUM G de R$24,00')
    print('-------------------------------------------------------')
    acumulador = acumulador + 24 #É somado o valor do acumulador mais o valor 24


  algo_mais = input('Deseja pedir mais alguma coisa? (S/N): ')
  algo_mais = algo_mais.upper()
  if algo_mais == 'S':
    continue #retorna para o início do programa
  else:
    print ('O total a ser pago é: R$ {:.2f}' .format(acumulador))
    break #finaliza o programa
    print(acumulador)

