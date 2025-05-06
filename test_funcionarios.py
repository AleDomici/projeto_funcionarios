import pytest
from unittest.mock import patch
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def test_calculo_bonus_funcionario_comum():
    funcionario = FuncionarioComum("Alice", 1000)
    assert funcionario.calcular_bonus() == 100

def test_calculo_bonus_gerente():
    gerente = Gerente("Bob", 2000, 500)
    assert gerente.calcular_bonus() == 900

def test_set_salario_negativo():
    funcionario = FuncionarioComum("Charlie", 1000)
    with pytest.raises(ValueError):
        funcionario.set_salario(-100)

@patch('builtins.print')
def test_mostrar_bonus(mock_print):
    sistema = SistemaRH()
    funcionario = FuncionarioComum("David", 1000)
    sistema.mostrar_bonus(funcionario)
    mock_print.assert_any_call("Funcionário: David, Bônus: 100.0")