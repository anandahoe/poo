from conta import Conta

class ContaPoupanca(Conta):
    """ContaPoupança representa uma conta poupança."""
    porcentagem = 0.58
    
    def total_conta_poupanca(self):
        self.saldo += self.balance * (ContaPoupanca.porcentagem / 100)
    
    def taxa_deposito(self) -> float:
        return 0.005
    
    