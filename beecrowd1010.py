cod1, num1, valor1 = input().split()
cod2, num2, valor2 = input().split()

valort = int(num1)*float(valor1) + int(num2)*float(valor2)

print(f"VALOR A PAGAR: R$ {valort:.2f}")