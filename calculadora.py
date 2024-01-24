def calculadora ():
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))
    operacao = input("Escolha a operação -> (+, -, *, /): ")

    if(operacao == "+" ):
        resultado = num1 + num2
        print(resultado)

    if(operacao == "-"):
      resultado = num1 - num2
      print(resultado)

    if(operacao == "*"):
       resultado = num1 * num2
       print(resultado)

    if(operacao == "/"):
       if num2 != 0:
           resultado = num1 / num2
           print(resultado)
       else:
           print("Não é possível realizar esta divisão, tente novamente com um número diferente de zero")
           return calculadora()

calculadora()