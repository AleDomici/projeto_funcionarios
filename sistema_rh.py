def logar_acao(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"Ação de log: {resultado}")
        return resultado
    return wrapper

class SistemaRH:
    @logar_acao
    def mostrar_bonus(self, funcionario):
        nome = funcionario.get_nome()
        bonus = funcionario.calcular_bonus()
        print(f"Funcionário: {nome}, Bônus: {bonus}")

    def __init__(self):
        self.funcionarios = []

    def cadastrar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_bonuses(self):
        for funcionario in self.funcionarios:
            self.mostrar_bonus(funcionario)