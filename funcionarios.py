from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    def get_nome(self):
        return self._nome

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        self._salario = salario

class FuncionarioComum(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus_adicional):
        super().__init__(nome, salario)
        self.bonus_adicional = bonus_adicional

    def calcular_bonus(self):
        return self._salario * 0.20 + self.bonus_adicional