import json
from typing import Any, NoReturn

import allure
import requests
from pydantic import ValidationError
from requests import ReadTimeout, Response

from autotests.pages.api.settings import REQUEST_MODELS_MAPPING, RESPONSE_MODELS_MAPPING


class API:
    def __init__(self) -> None:
        self.timeout = 60

    def make_request(
            self,
            method_type: str,
            url: str,
            method: str = '',
            body: Any = '',
            params: Any = '',
            headers: dict = '',
            negative: bool = False,
            expected_status_code: int = 400,
            response_status_validation: bool = True,
            response_validator: bool = True,
            request_validator: bool = False
    ) -> Response:
        """
        Method for receiving a request and response from the API.

        :param method_type: Type of method (POST, GET, PUT).
        :param url: Request url.
        :param method: Name of method from ENDPOINTS_MAPPING.
        :param body: Request body.
        :param params: Request parameters.
        :param headers: Request headers.
        :param negative: Negative flag for validation.
        :param expected_status_code: Expected status code.
        :param response_status_validation: Response status code validation.
        :param response_validator: Response body validation.
        :param request_validator: Request body validation.
        :return: Response body.
        """
        response = ''

        with allure.step(f'Request - {method_type}: {url} params: {params}'):
            try:
                if method_type == 'POST':
                    response = requests.post(
                        url=url, json=body, params=params, headers=headers, timeout=self.timeout)
                if method_type == 'GET':
                    response = requests.get(
                        url=url, params=params, headers=headers, timeout=self.timeout, json=body)
                if method_type == 'PUT':
                    response = requests.put(
                        url=url, json=body, params=params, headers=headers, timeout=self.timeout)
                if method_type == 'DELETE':
                    response = requests.delete(
                        url=url, params=params, headers=headers, timeout=self.timeout)
                if method_type == 'PATCH':
                    response = requests.patch(
                        url=url, json=body, params=params, headers=headers, timeout=self.timeout)
            except ReadTimeout:
                raise ReadTimeout(
                    f'Connection establishment time, limit value exceeded: {self.timeout} s.'
                )
            if response_status_validation:
                with allure.step('Checking response status'):
                    self.response_status_validation(
                        response, negative=negative, expected_status_code=expected_status_code)
                    with allure.step(f'Status: {response.status_code} {response.reason}.'):
                        pass
            if request_validator:
                with allure.step('Checking request body.'):
                    self.request_validator(response, method)
                    with allure.step(f'Request body:'):
                        with allure.step(str(response.request.body)):
                            pass
            if response_validator:
                with allure.step('Checking response body.'):
                    self.response_validator(response, method)
                    with allure.step(f'Response body: {str(response.json())}'):
                        # with allure.step(response.json()):
                        pass
        return response

    def request_validator(self, response: Response, method: str) -> NoReturn:
        """
        Request body validator.

        :param response: Response.
        :param method: Name of method from ENDPOINTS_MAPPING.
        """
        try:
            REQUEST_MODELS_MAPPING[method].model_validate(
                json.loads(response.request.body.decode('utf-8'))
            )
        except ValidationError as ve:
            raise Exception(
                self.api_error_handler(
                    url=response.url,
                    status=response.status_code,
                    request=response.request.body.decode('utf-8'),
                    response=response.json(),
                    error=ve.json()
                )
            )

    def response_validator(self, response: Response, method: str) -> NoReturn:
        """
        Response body validator.

        :param response: Response.
        :param method: Name of method from ENDPOINTS_MAPPING.
        """
        try:
            RESPONSE_MODELS_MAPPING[method].model_validate(response.json())
        except ValidationError as ve:
            raise Exception(
                self.api_error_handler(
                    url=response.url,
                    status=response.status_code,
                    request=response.request.body,
                    response=response.json(),
                    error=ve.json()
                )
            )

    def response_status_validation(
            self, response: Response, negative: bool, expected_status_code: int) -> NoReturn:
        """
        Response status code validation.

        :param response: Response.
        :param negative: For checking negative status code.
        :param expected_status_code: Expected status code.
        """
        status_code = response.status_code
        content_type = response.headers.get('content-type')

        if not content_type:
            res = ''
        elif 'application/json' in content_type and status_code != 500:
            res = response.json()
        else:
            res = response.text

        if negative:
            assert status_code == expected_status_code, AssertionError(
                self.api_error_handler(
                    url=response.url,
                    status=status_code,
                    request=response.request.body,
                    response=res
                )
            )

        if not negative:
            assert status_code in [200, 201, 204], AssertionError(
                self.api_error_handler(
                    url=response.url,
                    status=status_code,
                    request=response.request.body,
                    response=res
                )
            )

    @staticmethod
    def api_error_handler(
            url: str,
            status: int,
            request: Any = '',
            response: Any = '',
            error: Any = ''
    ) -> dict[str, Any]:
        """
        API error handler.

        :param url: Request url.
        :param status: Response status code.
        :param request: Request body.
        :param response: Response body.
        :param error: Error text.
        :return: Dict with error text.
        """
        error_data = {
            'URL': url,
            'Status': status
        }
        if request:
            error_data['Request'] = request
        if response:
            error_data['Response'] = response
        if error:
            error_data['Error'] = error
        return error_data
