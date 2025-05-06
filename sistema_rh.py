from typing import Callable
from funcionarios import Funcionario

def logar_acao(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"Ação logada: {func.__name__} foi chamada.")
        return resultado
    return wrapper

class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def cadastrar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    @logar_acao
    def mostrar_bonus(self, funcionario: Funcionario):
        """Mostra o bônus de um funcionário específico."""
        print(f"Nome: {funcionario.nome}, Bônus: {funcionario.calcular_bonus()}")

    def listar_bonuses(self):
        for funcionario in self.funcionarios:
            self.mostrar_bonus(funcionario)

def main():
    from funcionarios import FuncionarioComum, Gerente

    sistema = SistemaRH()
    funcionario1 = FuncionarioComum("Alice", 3000)
    gerente1 = Gerente("Bob", 5000, 1000)

    sistema.cadastrar_funcionario(funcionario1)
    sistema.cadastrar_funcionario(gerente1)

    print("Listando bônus dos funcionários:")
    sistema.listar_bonuses()

if __name__ == "__main__":
    main()