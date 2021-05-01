class Calculadora:
    def __init__(self, status):
        self.status = status

    def set_status(self, status):
        self.status = status.upper()
        if status == "ON":
            print("A calculadora está ligada, pode calcular.")
        elif status == "OFF":
            print("A calculadora está desligada.")
        else:
            print("Insira ON para ligar ou OFF para desligar.")

    def get_status(self):
        return self.status

    def operacao(self,opcao,num1, num2, resultado=0):
        if opcao == "+":
            resultado = self.soma(num1, num2)
        elif opcao == "-":
            resultado = self.subtracao(num1, num2)
        elif opcao == "*":
            resultado = self.multiplicacao(num1, num2)
        elif opcao == "/":
            resultado = self.divisao(num1, num2)
        elif opcao in "Xx":
            self.status == "OFF"
            return self.status
        elif opcao in "Cc":
            resultado = 0
            return resultado

        return resultado

    def soma(self, num1, num2):
        resultado = num1 + num2
        return resultado

    def subtracao(self, num1, num2):
        resultado = num1 - num2
        return resultado

    def multiplicacao(self, num1, num2):
        resultado = num1 * num2
        return resultado

    def divisao(self, num1, num2):
        resultado = num1 / num2
        return resultado




