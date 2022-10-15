#Entrada
numero = input('Digite o primeiro número ')
numero_1 = input('Digite o segundo número ')
operacao = input('Digite a operação: \n+ para Adição \n-para Subtração \n* para Mutiplicação \n/ para Divisão \n ')

#Processamento
equacao = f'{numero} {operacao} {numero_1}'
resultado = eval(equacao)

#Saida
print(f'{"-"*25} \nResultado: {resultado}\n{"-"*25}')