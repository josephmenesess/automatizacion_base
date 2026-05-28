import numpy as np
from src.melfa_kinematics.transforms import Rx, Ry, Rz, Trans

def test_rx_zero():
    assert np.allclose(Rx(0), np.eye(4))

def test_ry_zero():
    assert np.allclose(Ry(0), np.eye(4))

def test_rz_zero():
    assert np.allclose(Rz(0), np.eye(4))

def test_trans_zero():
    assert np.allclose(Trans(0,0,0), np.eye(4))

def test_trans_values():
    expected = np.array([
        [1,0,0,1],
        [0,1,0,2],
        [0,0,1,3],
        [0,0,0,1]
    ])

    assert np.allclose(Trans(1,2,3), expected)