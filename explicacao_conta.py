""" Implementação da conta."""

from __future__ import annotations

class Conta:
    """
    Conta representa uma conta bancária.

    Attributes:
        numero(str): Número indentificador da conta.
        titular(str): Nome do titular da conta.
        saldo(float): Saldo da conta.
        limite(float): Limite da conta.
    """
    quantidade_contas = 0 # Atributo estático -> Pertence a classe e não ao objeto.

    def __init__(self, numero: str, titular: str):
        # Realizando a validação do número da conta
        if len(numero) != 9:
            raise AttributeError("O número da conta deve possuir 9 digítos")
        
        # Encapsulamento
        self.__numero = numero

        # Ananda Hoefelmann  -> ananda hoefelmann ou ANANDA HOEFELMANN
        self.titular = titular #Está usando o @titular.setter para definir o valor

        self.__limite = 100
        self.__saldo = 0

        Conta.quantidade_contas +=1
        
    # Formata a visualização (print) do objeto
    def __str__(self):
        return f"Titular: {self.__titular} | Saldo: {self.__saldo} | Limite: {self.__limite}"


    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite: float):
        self.__limite = novo_limite

    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor: float) -> None:
        """Deposita um valor no saldo da conta.
        
        Args:
            valor(float): Valor do depósito.
        """
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta se o saldo + limite for maior ou igual o valor do saque
        
        Args:
            valor(float): Valor do saque;
            
        Returns:
            True se for bem-sucedido, False caso contrário.
        """
        if (self.__saldo + self.__limite) < valor:
            print("Saldo indisponível para realizar a operação")
            return False
        
        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor

        return True
    
    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """ Transfere o valor de uma conta para outra se o saldo + limite for maior ou igual ao valor do saque.

        Args:
            valor(float): Valor da transferência.
            conta_destino (Conta): Conta de destino da transferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")

    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        """Verifica se o número da conta é válido.
        
        Args:
            numero(str): Número da conta.
            
        Returns:
            True caso o número da conta seja válido, False caso contrário.
        """
        return len(numero) == 9

if __name__ == "__main__":
    conta_ananda = Conta("123456789", "ananda hoefelmann")

    print(f"Nome do titular quando foi criado: {conta_ananda.titular}")

    conta_ananda.titular = "ananda hoefelmann"
    
    print(f"Nome do titular após a modificação: {conta_ananda.titular}")
    
    print(f"Valor antes do depósito: {conta_ananda.saldo}")

    conta_ananda.depositar(100_000_000)

    print(f"Valor após o depósito: {conta_ananda.saldo}")

    conta_ananda.sacar(100_000_101)

    conta_ananda.sacar(1000)
    print(f"Valor após o saque {conta_ananda.saldo} | Limite {conta_ananda.limite}")

    conta_ananda.sacar(99999050)
    print(conta_ananda)

    conta_ananda.sacar(10)
    print(f"Valor após o saque {conta_ananda.saldo} | Limite {conta_ananda.limite}")

    conta_marcos = Conta("123123123", "marcos")
    print(conta_marcos)

    conta_ananda.transferir(20, conta_marcos)
    print(conta_marcos)
    print(conta_ananda)

    print(Conta.quantidade_contas)

    if (Conta.verifica_numero_conta("123654987")):
        print("O número da conta é válido!")
    else:
        print("O número da conta é inválido!")
