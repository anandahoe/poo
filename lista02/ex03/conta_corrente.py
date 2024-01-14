from conta import Conta

class ContaCorrente(Conta):
    """ContaCorrente representa uma conta corrente."""
    def __init__(self, titular: str, limite: float):
        super().__init__(titular)
        self.__limite = limite
    
    @property
    def limit(self):
        return self.__limit
    
    def sacar(self, quantia: float) -> bool:
        """Saca um valor da conta.

        Args:
            quantia (float): Valor que será sacado.

        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if self.saldo + self.__limite < quantia:
            print("Saldo Indisponível")
            return False
        
        if self.saldo < quantia:
            self.__limite -= quantia - self.saldo
            self.saldo = 0
        else:
            self.saldo -= quantia
        return True
    
    def taxa_deposito(self) -> float:
        return 0.002
    

if __name__ == "__main__":
    conta_corrente = ContaCorrente("Ananda", 100)
    conta_corrente.depositar(100)
    conta_corrente.sacar(20)
    print(conta_corrente)
    
    
        