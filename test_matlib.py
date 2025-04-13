# TESTY K MATEMATICKEJ KNIZNICI
# IVS - PROJEKT 2

# autor: Veronika Kocalkova (xkocalv00)
# TIM: VYDRYSEK

#funkcie vypisuju vysledky zaokruhlene na 13 desatinnych miest
#pridat assertions k funkciam na najvacsie a najmensie mozne cisla


from matlib import add, sub, mul, div, power, sqrt, fact #- dopisat nazov file s kniznicou a odkomentovat ked budu funkcie naimplementavane v kniznici 
#(da sa importnut pocas implementacie aj len funkcie, ktore uz su a ostatne zatial zakomentovat, aby testy prebehli)

import pytest
# test funkcie scitavanie
def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(-2, 3) == 1
    assert add(-2, -3) == -5
    assert add(2, -2) == 0
    assert add(-2, 2) == 0
    assert add(0, 0) == 0
    assert add(0.9999999999999, 0.9999999999999) == 1.9999999999998



# test funkcie odcitavanie
def test_sub():
    assert sub(3, 4) == -1
    assert sub(3, -4) == 7
    assert sub(-3, 4) == -7
    assert sub(-3, -4) == 1
    assert sub(3, 3) == 0
    assert sub(-3, -3) == 0
    assert sub(0, 0) == 0
    
    



# test funkcie nasobenie
def test_mul():
    assert mul(2, 3) == 6
    assert mul(2, -3) == -6
    assert mul(-2, 3) == -6
    assert mul(-2, -3) == 6
    assert mul(2, 0) == 0
    assert mul(0, 0) == 0
    assert mul(0.123456789, 0.0000003) == 0.0000000370370



# test funkcie delenie
def test_div():
    assert div(4, 2) == 2
    assert div(4, -2) == -2
    assert div(-4, 2) == -2
    assert div(-4, -2) == 2
    assert div(0, 2) == 0
    assert div(17, 24) == 0.7083333333333

    with pytest.raises(ZeroDivisionError):
        div(2, 0) 



# test funkcie umocnenie
def test_power():
    assert power(2, 0) == 1
    assert power(2, 1) == 2
    assert power(2, 2) == 4
    assert power(0.5, 2) == 0.25

    with pytest.raises(IncorrectExponentError):
        power(2, -1)

    with pytest.raises(IncorrectExponentError):
        power(2, 0.5)

    with pytest.raises(UndefinedResultError):
        power(0, 0)



# test funkcie odmocnenie (prvy argumet = zaklad, druhy argument = stupen odmocniny)
def test_sqrt():
    assert sqrt(4, 2) == 2
    assert sqrt(0.5, 2) == 0.7071067812
    assert sqrt(27, 3) == 3
    assert sqrt(0, 2) == 0
    assert sqrt(1, 2) == 1
    assert sqrt(1000000000, 31622.776601683)

    with pytest.raises(IncorrectRootError):
        sqrt(2, 0)
    with pytest.raises(IncorrectRootError):
        sqrt(2, 1)
    with pytest.raises(IncorrectRootError):
        sqrt(2, -2)
    with pytest.raises(IncorrectBaseError):
        sqrt(-1, 2)
    



# test funkcie faktorial
def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2

    with pytest.raises(IncorrectNumError):
        fact(-1)

    with pytest.raises(IncorrectNumError):
        fact(0.5)

    with pytest.raises(IncorrectNumError):
        fact(-0.5)



