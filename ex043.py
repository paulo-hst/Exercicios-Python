peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))

imc = peso / (altura*altura)
print('IMC: {:.2f}'.format(imc))

if imc <= 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')