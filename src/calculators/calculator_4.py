from typing import Dict, List

from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        mean = self.__process_data(input_data)

        formated_response = self.__format_response(mean)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("Body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        result = self.__driver_handler.mean(input_data)
        print(result)
        return result

    def __format_response(self, mean: float) -> Dict:
        return {"data": {"Calculator": 4, "result": mean}}
