from src.utils.operaciones import (
    sumar,
    restar,
    multiplicar,
    dividir
)

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 2) == 3

def test_multiplicar():
    assert multiplicar(4, 3) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    assert dividir(10, 0) == "Error: No se puede dividir por cero"