import glicko

def test_q():
    assert glicko.q == 0.0057565

def test_g():
    assert glicko.g(30) == 0.9955
    assert glicko.g(100) == 0.9531
    assert glicko.g(300) == 0.7242

def test_E():
    assert glicko.E(1500, 1400, 30) == 0.639
    assert glicko.E(1500, 1550, 100) == 0.432
    assert glicko.E(1500, 1700, 300) == 0.303

def test_d2():
    assert glicko.d2(1500, [(1400, 30, 1), (1550, 100, 0), (1700, 300, 0)]) == 53670.85

def test_outcome():
    assert glicko.outcome((1400, 80), (1500, 150)) == 0.376

def test_glicko():
    matches = [(1400, 30, 1), (1550, 100, 0), (1700, 300, 0)]
    assert glicko.glicko(1500, 200, matches) == (1464, 151.4)
