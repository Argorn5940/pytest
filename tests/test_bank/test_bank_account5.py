import pytest
from src.bank_account import BankAccount

@pytest.mark.raises
def test_withdraw_insufficient_balance():
  amount = BankAccount(500)
  with pytest.raises(ValueError, match="残高不足です"):
    amount.withdraw(501)
    
def test_deposit_positive_amount():
    amount = BankAccount(0)
    amount.deposit(500)
    assert amount.get_balance() == 500, "預金後の残高が間違っています"
    
@pytest.mark.skip(reason="作り途中です")
def test_feature_xx():
  #未実装のテスト
  pass

