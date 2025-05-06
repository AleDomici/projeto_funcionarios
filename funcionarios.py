from abc import ABC, abstractmethod
from typing import List

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float):
        self._nome = nome
        self._salario = salario

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, valor: float):
        if valor < 0:
            raise ValueError("Salário não pode ser negativo.")
        self._salario = valor

    @abstractmethod
    def calcular_bonus(self) -> float:
        pass

class FuncionarioComum(Funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, bonus_adicional: float = 0):
        super().__init__(nome, salario)
        self._bonus_adicional = bonus_adicional

    def calcular_bonus(self) -> float:
        return self.salario * 0.20 + self._bonus_adicional