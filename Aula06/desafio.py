def multa(x):
    pesoLimite = 100
    pesoExcedente = float(x - pesoLimite)
    valorAPagar = pesoExcedente * 4
    return print(f"Você deverá pagar o valor da multa de R$ {valorAPagar:.2f}")

pesoPeixes = float(input("Digite o peso da quantidade total dos peixes pescados (kg): "))

if pesoPeixes > 100:
    multa(pesoPeixes)
else:
    print("O peso está dentro do limite. Você não pagará multa.")