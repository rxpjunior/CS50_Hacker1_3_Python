"Programa CS50_Hacker1_3_Python"

#Entrando e testando os valores
while True:
    temp=input("Entre com o valor de MF: ")
    try:
        mf = int(temp)     
        break
    except:
        print("O valor deve ser um inteiro")

while True:
    temp=input("Entre com o valor de FM: ")
    try:
        fm = int(temp)
        break
    except:
        print("O valor deve ser um inteiro")

while True:
    temp=input("Entre com o valor de FF: ")
    try:
        ff = int(temp)
        break
    except:
        print("O valor deve ser um inteiro")

while True:
    temp=input("Entre com o valor de MM: ")
    try:
        mm = int(temp)
        break
    except:
        print("O valor deve ser um inteiro")

#Soma dos valores
soma=mf+fm+ff+mm

#Percentuais a serem usados. Eles são areedondados. 20 é o numero maximo de caraceres da barra
temp=20/soma*mf
percentMf=int(temp)

temp=20/soma*fm
percentFm=int(temp)

temp=20/soma*mm
percentMm=int(temp)

temp=20/soma*ff
percentFf=int(temp)

#Formacao e exibicao dos resultados
graficoMf='M-F: '
graficoFm='F-M: '
graficoFf='F-F: '
graficoMm='M-M: '
for x in range(percentMf):
    graficoMf=graficoMf+'#'

graficoFm='F-M: '
for x in range(percentFm):
    graficoFm=graficoFm+'#'

graficoMm='M-M: '
for x in range(percentMm):
    graficoMm=graficoMm+'#'

graficoFf='F-F: '
for x in range(percentFf):
    graficoFf=graficoFf+'#'

print('\n',graficoMf)
print('\n',graficoFm)
print('\n',graficoFf)
print('\n',graficoMm)
