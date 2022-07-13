import datetime
from decimal import Decimal
from unicodedata import decimal
from numpy import datetime64, float64
import pytest
import pandas as pd
data = pd.read_csv('HINDALCO.csv', index_col=False, delimiter = ',')


def test_string():
    """
    The function tests the validity of 
    
    """
    for i in data['instrument']:
        assert type(i) == str

def test_volume_int():
    """
    The function tests the validity of
    
    """
    for i in data['volume']:
        assert type(i) == int

def test_close_decimal():
    """
    The function tests the validity of
    
    """
    for i in data['close']:
        assert type(Decimal(i)) == Decimal


def test_open_decimal():
    """
    The function tests the validity of
    
    """
    for i in data['open']:
        assert type(Decimal(i)) == Decimal

def test_high_decimal():
    """
    The function tests the validity of
    
    """
    for i in data['high']:
        assert type(Decimal(i)) == Decimal

def test_low_decimal():
    """
    The function tests the validity of
    
    """
    for i in data['low']:
        assert type(Decimal(i)) == Decimal  

def test_datetime():
    """
    The function tests the validity of
    
    """
    for i in data['datetime']:
        format = '%Y-%m-%d %H:%M:%S'
        i = datetime.datetime.strptime(i, format)
        assert type(i) == datetime.datetime

if __name__ == '__main__':
    unittest.main()