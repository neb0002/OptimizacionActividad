import pytest
from optimizar import ClaseOptimizar

def test_arrNumeros():
    optimizar = ClaseOptimizar()
    assert len(optimizar.ArrNumeros())==0
    optimizar.add(3)
    assert len(optimizar.ArrNumeros())==1

def test_add():
    optimizar = ClaseOptimizar()
    optimizar.ArrNumeros().clear()
    assert len(optimizar.ArrNumeros())==0


def test_media():
    optimizar = ClaseOptimizar()
    optimizar.ArrNumeros().clear()
    assert len(optimizar.ArrNumeros())==0
    optimizar.add(5)
    optimizar.add(5)
    optimizar.add(5)
    assert len(optimizar.ArrNumeros())==3
    assert optimizar.media()==5.0