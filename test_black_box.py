# from app import add
# def test_add_positive_numbers():
#     assert add(10, 20) == 30
# def test_add_zero_values():
#     assert add(0, 0) == 0
# def test_add_negative_numbers():
#     assert add(-5, 5) == 0


import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

# ---------------- Deposit Tests ----------------

@pytest.mark.parametrize("balance, amount, expected", [
    (1000, 500, 1500),
    (0, 100, 100),
])
def test_deposit_positive(balance, amount, expected):
    assert deposit(balance, amount) == expected

@pytest.mark.parametrize("balance, amount", [
    (1000, 0),
    (1000, -200),
])
def test_deposit_invalid(balance, amount):
    with pytest.raises(ValueError):
        deposit(balance, amount)

# ---------------- Withdraw Tests ----------------

def test_withdraw_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(500, 600)

# ---------------- Transfer Tests ----------------

def test_transfer_success():
    from_acc, to_acc = transfer(1000, 500, 300)
    assert from_acc == 700
    assert to_acc == 800

def test_transfer_failure():
    with pytest.raises(ValueError):
        transfer(200, 500, 300)

# ---------------- Interest Calculation ----------------

def test_interest_calculation():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00

# ---------------- Loan Eligibility ----------------

@pytest.mark.parametrize("balance, score, expected", [
    (6000, 750, True),
    (4000, 750, False),
    (6000, 650, False),
])
def test_loan_eligibility(balance, score, expected):
    assert check_loan_eligibility(balance, score) == expected
