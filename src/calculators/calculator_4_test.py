from typing import Dict, List

from .calculator_4 import Calculator4


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def mean(self, numbers: List[float]) -> float:
        return 3


def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})

    calculator_4 = Calculator4(MockDriverHandler())
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 4, "result": 3}}
