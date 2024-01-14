"""3) Crie uma superclasse Conta com os seguintes atributos:
número da conta, titular e saldo.
Essa superclasse deve implementar os seguintes métodos: depositar(), sacar(), transferir().
Implemente as subclasses: ContaCorrente (Possui um limite adicional para saque e transferências),
ContaPoupança (Gera juros mensalmente), ContaInvestimento (Permite investir em ações).
Cada conta possui uma taxa diferente para depósito conforme abaixo:
Conta corrente: 0.2%
Conta poupança: 0.5%
Conta investimento: 0.8%
"""
from __future__ import annotations
from random import randint
from abc import ABC, abstractmethod

class Conta(ABC):
    """Conta representa uma conta bancária.

    Args:
        titular (str): Nome do titular da conta.
    """

    def __init__(self, titular: str):
        self.__numero = randint(1, 100_000)
        self.titular = titular
        self.__saldo = 0
        
    def __str__(self):
        return f"Titular: {self.titular} | Saldo: {self.__saldo}"

    @property
    def numero_conta(self):
        """(int): Número da conta."""
        return self.__numero

    @property
    def saldo(self):
        """(float): Saldo da conta."""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo.")
            self.__saldo= valor

    def sacar(self, quantia: float) -> bool:
        """Saca um valor da conta.

        Args:
            quantia (float): Valor que será sacado.

        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if self.__saldo >= quantia:
            self.__saldo -= quantia
            return True
        
        return False
        

    def depositar(self, quantia: float):
        """Deposita um valor na conta.
        
        Args:
            quantia (float): Valor que será depositado na conta.
        """
        taxa = self.taxa_deposito()
        
        self.__saldo += quantia * (1 - taxa)
        
    def transferir(self, quantia: float, conta_transferencia: Conta):
        """Transfere um valor para outra conta.
        
        Args: 
            quantia (float): Valor que será transferido.
            conta_transferencia (Conta): Conta de destino da transferência.
        """
        if (self.sacar(quantia)):
            conta_transferencia.depositar(quantia)
        else:
            print("Não foi possível realizar a transferência: Saldo indisponível.")
            
    @abstractmethod
    def taxa_deposito(self) -> float:
        """Obtém a taxa de depósito da conta bancária."""

 