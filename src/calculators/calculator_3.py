from typing import Dict, List

from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntity


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplacation(input_data)
        self.__varify_results(variance, multiplication)

        formated_response = self.__format_response(variance)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("Body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplacation(self, numbers: List[float]) -> float:
        multiplication = 1.0
        for num in numbers:
            multiplication *= num

        return multiplication

    def __varify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequest("Falha no processo: Variância menor que multiplicação")

    def __format_response(self, variance: float) -> Dict:
        return {"data": {"Calculator": 3, "value": variance, "successs": True}}
