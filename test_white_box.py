# import pytest
# from app import divide
# def test_divide_valid_branch():
#     assert divide(10, 2) == 5
# def test_divide_exception_branch():
#     with pytest.raises(ValueError):
#         divide(10, 0)


import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

# ---------------- Deposit White-Box ----------------

def test_deposit_error_branch():
    with pytest.raises(ValueError):
        deposit(1000, -50)


# ---------------- Withdraw White-Box ----------------

def test_withdraw_negative_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -10)


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(100, 200)


# ---------------- Transfer White-Box ----------------

def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -100)


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(100, 500, 200)


def test_transfer_success_path():
    result = transfer(500, 300, 100)
    assert result == (400, 400)


# ---------------- Interest White-Box ----------------

def test_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)


def test_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)


def test_interest_valid_path():
    assert calculate_interest(1000, 10, 1) == 1100
