from conta import Conta

class ContaInvestimento(Conta):
    """Conta Investimento representa uma conta de investimento.""" 
    porcentagem = 0.8   
    
    def __init__(self, titular: str):
        super().__init__(titular)
        self.__quantia_investida = 0

    
    def taxa_deposito(self) -> float:
        return 0.008
    
    def investir_acoes(self, quantia: float):
        if (self.sacar(quantia)):
            self.__quantia_investida += quantia
            
    def total_conta_investimento(self):
        self.saldo += self.__quantia_investida * (ContaInvestimento.porcentagem / 100)
    
        
    
    
        