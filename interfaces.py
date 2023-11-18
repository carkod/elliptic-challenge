class AccountBalance:
    account: str
    balance: str

class BalanceResponse:
    status: str
    message: str
    result: list[AccountBalance]

    def __init__(self, status, message, result) -> None:
        self.status = status
        self.message = message
        self.result = result
        return __dict__
