import pytest
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def test_funcionario_comum_bonus():
    funcionario = FuncionarioComum("Alice", 3000)
    assert funcionario.calcular_bonus() == 300

def test_gerente_bonus():
    gerente = Gerente("Bob", 5000, 1000)
    assert gerente.calcular_bonus() == 2000

def test_salario_negativo():
    funcionario = FuncionarioComum("Alice", 3000)
    with pytest.raises(ValueError):
        funcionario.salario = -100

def test_mostrar_bonus(capfd):
    funcionario = FuncionarioComum("Alice", 3000)
    sistema = SistemaRH()
    sistema.mostrar_bonus(funcionario)
    out, err = capfd.readouterr()
    assert "Nome: Alice, Bônus: 300.0" in out