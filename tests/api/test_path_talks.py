import os
import random

import allure
import pytest
from dotenv import load_dotenv

from autotests.pages.api.api_utils import API
from autotests.pages.api.settings import ENDPOINTS_MAPPING
from autotests.pages.data.test_data import TestData
from autotests.pages.utils import slack_post_msg, get_text_blocks, token_decode

load_dotenv()
API_URL = os.environ["PATH_TALKS_API_URL"]

@allure.feature('API Path Talks')
@allure.suite('Path Talks')
class TestApiPathTalks:
    @allure.story('Path Talks')
    @allure.title('Checking POST: /clients')
    @allure.label('layer', 'api_tests')
    def test_api_post_clients(self, config):
        """ Checking POST: /clients - """
        api = API()
        method = 'clients'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        body = {
            "name": name,
            "brandId": config.path_talks_data['brand_id']['positive_1']
        }
        res = api.make_request(
            method_type='POST', url=url, method=method, body=body, headers=headers)

        assert res.json()['name'] == name, {'as_is': res.json()['name'], 'to_be': name}

    @allure.story('Path Talks')
    @allure.title('Checking POST: /clients [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('empty_name', '', 422),
            ('integer_name', 111, 422),
            ('name_longer_than_256', '', 422),
            ('empty_body', '', 422),
            ('duplicate_name', 'test', 409),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'DELETE', 405)
        ]
    )
    def test_api_post_clients_negative(self, case: str, value: str, code: int, config):
        """ Checking POST: /clients [negative] - """
        api = API()
        method = 'clients'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        if case == 'name_longer_than_256':
            value = 'a' * 257
        body = '' if case == 'empty_body' else {
            "name": value,
            "brandId": config.path_talks_data['brand_id']['positive_1']
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking POST: /clients/client_id/auth-tokens')
    @allure.label('layer', 'api_tests')
    def test_api_post_clients_auth_tokens(self, config):
        """ Checking POST: /clients/client_id/auth-tokens - """
        api = API()
        method = 'auth_tokens'
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {"description": TestData().words()}
        res = api.make_request(
            method_type='POST', url=url, method=method, body=body, headers=headers)

        sub = token_decode(token=res.json()['jwt'])['sub']

        assert sub == client_id, {'as_is': sub, 'to_be': client_id}

    @allure.story('Path Talks')
    @allure.title('Checking POST: /clients/client_id/auth-tokens [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('integer_desc', 111, 422),
            ('empty_body', '', 422),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'DELETE', 405),
            ('incorrect_client_id', '018f3a02-4719-700b-b57b-79ccf8cc3b71', 404)
        ]
    )
    def test_api_post_clients_auth_tokens_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking POST: /clients/client_id/auth-tokens [negative] - """
        api = API()
        method = 'auth_tokens'
        client_id = value if case == 'incorrect_client_id' else \
            config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = '' if case == 'empty_body' else {"description": value}
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE: /clients/client_id/auth-tokens/token_id')
    @allure.label('layer', 'api_tests')
    def test_api_delete_clients_auth_tokens(self, config):
        """ Checking DELETE: /clients/client_id/auth-tokens/token_id - """
        api = API()
        method = 'auth_tokens'
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {"description": TestData().words()}
        res = api.make_request(
            method_type='POST', url=url, method=method, body=body, headers=headers)

        token_id = res.json()['id']

        method_delete = 'delete_auth_tokens'
        url_delete = API_URL + ENDPOINTS_MAPPING[method_delete].format(
            client_id=client_id, token_id=token_id)
        api.make_request(
            method_type='DELETE',
            url=url_delete,
            method=method_delete,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE: /clients/client_id/auth-tokens/token_id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
            ('deleted_token_id', '', 404)
        ]
    )
    def test_api_delete_clients_auth_tokens_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking DELETE: /clients/client_id/auth-tokens/token_id [negative] - """
        api = API()
        client_id = config.path_talks_data['client_id']['positive_main']
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''

        token_id = config.path_talks_data['client_id']['positive_1']

        method_delete = 'delete_auth_tokens'
        url_delete = API_URL + ENDPOINTS_MAPPING[method_delete].format(
            client_id=client_id, token_id=token_id)
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'DELETE',
            url=url_delete,
            method=method_delete,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET: /clients [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 100000000)
        ]
    )
    def test_api_get_clients(self, case: str, value: str):
        """ Checking GET: /clients - """
        api = API()
        method = 'get_clients'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        res = api.make_request(
            method_type='GET', url=url, method=method, headers=headers, params=params)

        limit_res = res.json()['pagination']['limit']
        offset_res = res.json()['pagination']['offset']
        items_count = len(res.json()['items'])

        if case == 'without_params':
            assert limit_res == 10, {'as_is': limit_res, 'to_be': 10}
            assert offset_res == 0, {'as_is': offset_res, 'to_be': 0}
        if case in ['with_limit', 'with_offset_and_limit']:
            assert limit_res == limit, {'as_is': limit_res, 'to_be': limit}
            assert items_count == limit, {'as_is': items_count, 'to_be': limit}
        if case in ['with_offset', 'with_offset_and_limit']:
            assert offset_res == offset, {'as_is': offset_res, 'to_be': offset}
        if case == 'with_max_limit':
            assert limit_res == 100, {'as_is': limit_res, 'to_be': 100}
        if case == 'with_max_offset':
            assert limit_res == 10, {'as_is': limit_res, 'to_be': 10}
            assert offset_res == value, {'as_is': offset_res, 'to_be': value}
            assert items_count == 0, {'as_is': items_count, 'to_be': 0}

    @allure.story('Path Talks')
    @allure.title('Checking GET: /clients [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_get_clients_negative(self, case: str, value: str | int, code: int):
        """ Checking GET: /clients [negative] - """
        api = API()
        method = 'clients'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET: /clients/client_id')
    @allure.label('layer', 'api_tests')
    def test_api_get_clients_by_id(self):
        """ Checking GET: /clients/client_id - """
        api = API()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        method_clients = 'get_clients'
        url_clients = API_URL + ENDPOINTS_MAPPING[method_clients]

        res_clients = api.make_request(
            method_type='GET', url=url_clients, method=method_clients, headers=headers)

        clients = res_clients.json()['items']
        random_client = random.choice(clients)
        client_id = random_client['id']

        method = 'get_clients_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        res = api.make_request(method_type='GET', url=url, method=method, headers=headers)

        assert client_id == res.json()['id'], {'as_is': client_id, 'to_be': res.json()['id']}

    @allure.story('Path Talks')
    @allure.title('Checking GET: /clients/client_id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_id', '018f33dd-b739-7066-a5b7-6f2024f3494s', 404),
            ('incorrect_method', 'POST', 405),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_get_clients_by_id_negative(self, case: str, value: str | int, code: int):
        """ Checking GET: /clients/client_id [negative] - """
        api = API()
        method = 'get_clients_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=value)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}

        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking PUT: /clients/client_id/status [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('active_status', 'active'),
            ('inactive_status', 'inactive')
        ]
    )
    def test_api_put_clients_status(self, case: str, value: str, config):
        """ Checking PUT: /clients/client_id/status - """
        api = API()
        method = 'put_client_status'
        client_id = config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {"status": value}
        res = api.make_request(
            method_type='PUT', url=url, method=method, body=body, headers=headers)

        assert res.json()['status'] == value, {'as_is': res.json()['status'], 'to_be': value}

    @allure.story('Path Talks')
    @allure.title('Checking PUT: /clients/client_id/status [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('empty_status', '', 422),
            ('integer_status', 111, 422),
            ('empty_body', '', 422),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
        ]
    )
    def test_api_put_clients_status_negative(self, case: str, value: str, code: int, config):
        """ Checking PUT: /clients/client_id/status [negative] - """
        api = API()
        method = 'put_client_status'
        client_id = config.path_talks_data['client_id']['positive_1'] \
            if case == 'inactive_status_my_self' else \
            config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = '' if case == 'empty_body' else {"status": value}
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks')
    @allure.title('Checking PUT: /clients/client_id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('name', 'TestClientSS'),
            #('different_client', 'AutoTest123')
        ]
    )
    def test_api_put_clients_name(self, case: str, value: str, config):
        """ Checking PUT: /clients/client_id - """
        api = API()
        method = 'get_clients_id'
        client_id = config.path_talks_data['client_id']['positive_1'] if case == 'different_client' \
            else config.path_talks_data['client_id']['positive_3']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {"name": value}
        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers
        )

    @allure.story('Path Talks')
    @allure.title('Checking PUT: /clients/client_id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('Existing_client', 'Laurine_Stokes73', 409),
            ('empty_name', '', 422),
            ('massive_name', [], 422),
            ('int_name', 111, 422),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
            ('incorrect_client_id', '018f3a02-4719-700b-b57b-79313313b71', 404),
            ('name_longer_than_256', '', 422)
        ]
    )
    def test_api_put_clients_name_negative(self, case: str, value: str, code: int, config):
        """ Checking PUT: /clients/client_id [negative] - """
        api = API()
        method = 'get_clients_id'
        client_id = value if case == 'incorrect_client_id' else \
            config.path_talks_data['client_id']['positive_3']
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        if case == 'name_longer_than_256':
            value = 'a' * 257
        body = {"name": value}
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /clients/client_id/roles [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('role_admin', '018ee3f9-3793-703d-903e-c8420162c308'),
            ('role_admin_and_user', '018f4c68-ead3-724b-9c82-059f3db5cc95'),
            ('empty_role', '018f517f-ca0c-7019-8a61-34d3185a4b4d'),
            ('user_role', '018f2d5e-4310-723a-ab5e-4593bca509f3')
        ]
    )
    def test_api_get_clients_roles(self, case: str, value: str):
        """ Checking GET /clients/client_id/roles - """
        api = API()
        method = 'get_client_roles'
        client_id = value
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /clients/client_id/roles [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('empty_client_id', '', 404),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
            ('incorrect_client_id', '018f3a02-4719-700b-b57b-79313313b71', 404),
            ('inactive_status_client', '018f350b-e88e-7179-b602-b7798c1df9e8', 404)
        ]
    )
    def test_api_get_clients_roles_negative(self, case: str, value: str, code: int):
        """ Checking GET /clients/client_id/roles [negative] - """
        api = API()
        method = 'get_client_roles'
        client_id = value if case == 'incorrect_client_id' else \
            '123'
        url = API_URL + ENDPOINTS_MAPPING[method].format(client_id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks')
    @allure.title('Checking POST /clients/client_id/roles/role [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, role',
        [
            ('add_role_user', '018f2e46-e696-73bf-b471-8eb1526ff841', 'user'),
            ('add_role_admin', '018f33dd-b739-7066-a5b7-6f2024f3494c', 'admin'),
            ('add_role_user_(2 roles)', '018f3506-96ef-735f-a24e-815df0bdb5e0', 'user'),
            ('add_role_admin_(2 roles)', '018f3506-96ef-735f-a24e-815df0bdb5e0', 'admin')
        ]
    )
    def test_api_post_clients_roles(self, case: str, value: str, role: str):
        """ Checking POST /clients/client_id/roles/role - """
        api = API()
        method = 'post_client_roles'
        client_id = value
        role = role
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            client_id=client_id, role=role)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )
        method_delete = 'delete_client_roles'
        client_id = value
        role = role
        url = API_URL + ENDPOINTS_MAPPING[method_delete].format(
            client_id=client_id, role=role)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='DELETE',
            url=url,
            method=method_delete,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking POST /clients/client_id/roles/role [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, role, code',
        [
            ('non-existent_role', '018f2e46-e696-73bf-b471-8eb1526ff841', 'testerone', 404),
            ('add_role_inactive_client', '018f3510-c25b-72e8-bf90-b27d256ef2fe', 'admin', 404),
            ('add_role_user_again', '018f2d5e-4310-723a-ab5e-4593bca509f3', 'user', 409),
            ('add_empty_role ', '018f3506-96ef-735f-a24e-815df0bdb5e0', '', 404),
            ('add_role_id_token', '018f7ad4-07f4-709c-b4e2-c847e7350a3b', 'admin', 404),
            ('incorrect_method', 'GET', 'user', 405),
            ('without_auth_token', '018f3506-96ef-735f-a24e-815df0bdb5e0', 'user', 401)
        ]
    )
    def test_api_post_clients_roles_negative(
            self,
            case: str,
            value: str,
            role: str,
            code: int
    ):
        """ Checking POST /clients/client_id/roles/role [negative] - """
        api = API()
        method = 'post_client_roles'
        client_id = value
        role = role
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            client_id=client_id, role=role)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            headers=headers,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE /clients/client_id/roles/role [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, role',
        [
            ('role_user', '018f3df3-d498-7269-aee5-ef9dd992e415', 'user'),
            ('role_admin', '018f3ebb-7458-70b5-ac75-e39b7c663389', 'admin'),
            ('role_user_(2 roles)', '018f3ebf-5833-73c6-b3d1-da45f8d4562d', 'user'),
            ('role_admin_(2 roles)', '018f3ebf-5833-73c6-b3d1-da45f8d4562d', 'admin')
        ]
    )
    def test_api_delete_clients_roles(self, case: str, value: str, role: str):
        """ Checking DELETE /clients/client_id/roles/role - """

        api = API()
        method = 'post_client_roles'
        client_id = value
        role = role
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            client_id=client_id, role=role)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            headers=headers,
            response_validator=False)

        method_delete = 'delete_client_roles'
        client_id = value
        role = role
        url = API_URL + ENDPOINTS_MAPPING[method_delete].format(
            client_id=client_id, role=role)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='DELETE',
            url=url,
            method=method_delete,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE /clients/client_id/roles/role [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, role, code',
        [
            ('delete_non-existent_role', '018f2e46-e696-73bf-b471-8eb1526ff841', 'testerone', 404),
            #('delete_role_my_self', '018ee3f9-3793-703d-903e-c8420162c308', 'admin', 403), #TODO need fix
            ('incorrect_method', 'GET', 'user', 405),
            ('delete_empty_role', '018f3506-96ef-735f-a24e-815df0bdb5e0', '', 404),
            ('without_auth_token', '018f3506-96ef-735f-a24e-815df0bdb5e0', 'user', 401)
        ]
    )
    def test_api_delete_clients_roles_negative(
            self,
            case: str,
            value: str,
            role: str,
            code: int
    ):
        """ Checking DELETE /clients/client_id/roles/role [negative] - """
        api = API()
        method = 'delete_client_roles'
        client_id = value
        role = role
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            client_id=client_id, role=role)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'DELETE',
            url=url,
            method=method,
            headers=headers,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking POST /sms/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('gateway_twilio', ''),
            ('gateway_dummy', '')
        ]
    )
    def test_api_post_sms_account(
            self,
            value,
            case,
            config
    ):
        """ Checking POST /sms/accounts - """
        api = API()
        method = 'post_sms_account'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        body = {
            "name": name,
            "description": "123",
            "brandId": config.path_talks_data['brand_id']['positive_2'],
            "gatewayType": "dummy",
            "settings": {
                "dispatchStatus": {
                    "status": "sent",
                    "code": 201
                    },
                "deliveryStatus": {
                    "status": "delivered",
                    "code": 204
                },
            }
        } if case == 'gateway_dummy' else {
                "name": name,
                "description": "321",
                "brandId": config.path_talks_data['brand_id']['positive_2'],
                "gatewayType": "twilio",
                "settings": {
                    "accountSid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    "accountToken": "2eac8346e40cb2c8a74425dd859f79ea1"
                }
        }
        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            headers=headers,
            body=body,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking POST /sms/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('duplicate_name', 'Jewell', 409),
            ('empty_body', '', 422),
            ('incorrect_method', 'PUT', 405),
            ('without_auth_token', '', 401),
            ('name_longer_than_256', '', 422)
        ]
    )
    def test_api_post_sms_account_negative(self, case: str, value: str, code: int, config):
        """ Checking POST /sms/accounts [negative] - """
        api = API()
        method = 'post_sms_account'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        if case == 'name_longer_than_256':
            value = 'a' * 257
        name = value
        body = '' if case == 'empty_body' else {
            "name": name,
            "description": "321",
            "brandId": config.path_talks_data['brand_id']['positive_2'],
            "gatewayType": "twilio",
            "settings": {
                "accountSid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "accountToken": "2eac8346e40cb2c8a74425dd859f79ea1"
            }
        }
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            headers=headers,
            body=body,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PUT /sms/accounts/id/status [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('inactive_status', 'inactive'),
            ('active_status', 'active')
        ]
    )
    def test_api_put_sms_account_status(self, case: str, value: str, config):
        """ Checking PUT /sms/accounts/id/status - """
        api = API()
        account_sms_id = config.path_talks_data['account_sms_id']['positive_1']
        method = 'put_sms_account_status'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=account_sms_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {"status": value}
        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            headers=headers,
            body=body,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PUT /sms/accounts/id/status [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('empty_body', '', 422),
            ('incorrect_method', 'POST', 405),
            ('without_auth_token', '', 401),
            ('incorrect_account_id', '01241237f-23fe-7028-b331-b88eef1e1e3e', 404)
        ]
    )
    def test_api_put_sms_account_status_negative(self, case: str, value: str, code: int, config):
        """ Checking PUT /sms/accounts/id/status [negative] - """
        api = API()
        account_sms_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['account_sms_id']['positive_1']
        method = 'put_sms_account_status'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=account_sms_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = '' if case == 'empty_body' else {"status": value}
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            headers=headers,
            body=body,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PUT /sms/accounts/id')
    @allure.label('layer', 'api_tests')
    def test_api_put_sms_account(self, config):
        """ Checking PUT /sms/accounts/id - """
        api = API()
        account_sms_id = config.path_talks_data['account_sms_id']['positive_2']
        method = 'put_sms_account'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=account_sms_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        body = {
            "name": name,
            "description": "123",
            "gatewayType": "twilio",
            "settings": {
                "accountSid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "accountToken": "54321346e40cb2c8a74425dd859f79ea1"
            }
        }
        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            headers=headers,
            body=body,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PUT /sms/accounts/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('duplicate_name', '', 409),
            ('empty_body', '', 422),
            ('without_auth_token', '', 401),
            ('incorrect_account_id', '01241237f-23fe-7028-b331-b88eef13515', 404)
        ]
    )
    def test_api_put_sms_account_negative(self, case: str, value: str, code: int, config):
        """ Checking PUT /sms/accounts/id [negative] - """
        api = API()
        account_sms_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['account_sms_id']['positive_2']
        method = 'put_sms_account'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=account_sms_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        name = 'Jewell' if case == 'duplicate_name' else TestData().first_name()
        body = '' if case == 'empty_body' else {
            "name": name,
            "description": "123",
            "gatewayType": "twilio",
            "settings": {
                "accountSid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "accountToken": "54321346e40cb2c8a74425dd859f79ea1"
            }
        }
        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            headers=headers,
            body=body,
            response_validator=False,
            negative=True,
            expected_status_code=code
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_sms_account(self, case: str, value: str, ):
        """ Checking GET /sms/accounts - """
        api = API()
        method = 'get_sms_accounts'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_get_sms_account_negative(self, case: str, value: str, code: int, ):
        """ Checking GET /sms/accounts [negative] - """
        api = API()
        method = 'get_sms_accounts'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/accounts/id')
    @allure.label('layer', 'api_tests')
    def test_api_get_sms_account_id(self, config):
        """ Checking GET /sms/accounts/id - """
        api = API()
        account_sms_id = config.path_talks_data['account_sms_id']['positive_2']
        method = 'get_sms_accounts_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=account_sms_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/accounts/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_account_id', '01241237f-23fe-7028-b331-b88eef13515', 404),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_get_sms_account_id_negative(self, case: str, value: str, code: int, config):
        """ Checking GET /sms/accounts/id [negative] - """
        api = API()
        account_sms_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['account_sms_id']['positive_2']
        method = 'get_sms_accounts_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=account_sms_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /clients/client_id/auth-tokens/id')
    @allure.label('layer', 'api_tests')
    def test_api_get_client_auth_token_id(self, config):
        """ Checking GET /clients/client_id/auth-tokens/id - """
        api = API()
        method = 'get_client_auth_token_id'
        client_id = config.path_talks_data['client_id']['positive_4']
        token_id = config.path_talks_data['token_client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id, id=token_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /clients/client_id/auth-tokens/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
            ('not_uuid_format_token_id', '12341551-1f3e-1453-b9e6-2a87c18e004f', 404),
            ('incorrect_token_id', '0901042-1f3e-73e7-b9e6-2a87c18e004f', 404),
            ('incorrect_client_id', '018f2d5e-7956-723a-ab5e-4593bca509f3', 404)

        ]
    )
    def test_api_get_client_auth_token_id_negative(self, case: str, value: str, code: int, config):
        """ Checking GET /clients/client_id/auth-tokens/id [negative] - """
        api = API()
        method = 'get_client_auth_token_id'
        client_id = value if case == 'incorrect_client_id' \
            else config.path_talks_data['client_id']['positive_4']
        token_id = value if case == 'incorrect_token_id' or case == 'not_uuid_format_token_id' \
            else config.path_talks_data['token_client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id, id=token_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /clients/client_id/auth-tokens [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_client_auth_token(self, case: str, value: str, config):
        """ Checking GET /clients/client_id/auth-tokens - """
        api = API()
        method = 'get_client_auth_token'
        client_id = config.path_talks_data['client_id']['positive_4']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /clients/client_id/auth-tokens [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
            ('incorrect_client_id', '1231233-7956-723a-ab5e-4593bca509f3', 404),
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401)

        ]
    )
    def test_api_get_client_auth_token_negative(self, case: str, value: str, code: int, config):
        """ Checking GET /clients/client_id/auth-tokens [negative] - """
        api = API()
        method = 'get_client_auth_token'
        client_id = value if case == 'incorrect_client_id' \
            else config.path_talks_data['client_id']['positive_4']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking GET /brands [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_brand(self, case: str, value: str):
        """ Checking GET /brands - """
        api = API()
        method = 'get_brands'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking GET /brands [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401)

        ]
    )
    def test_api_get_brand_negative(self, case: str, value: str, code: int):
        """ Checking GET /brands [negative] - """
        api = API()
        method = 'get_brands'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking GET /brands/id')
    @allure.label('layer', 'api_tests')
    def test_api_get_brand_id(self, config):
        """ Checking GET /brands/id - """
        api = API()
        brand_id = config.path_talks_data['brand_id']['positive_1']
        method = 'get_brands_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=brand_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking GET /brands/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
            ('incorrect_client_id', '018f2d5e-7956-723a-ab5e-4593bca509f3', 404)
        ]
    )
    def test_api_get_brand_id_negative(self, case: str, value: str, code: int):
        """ Checking GET /brands/id [negative] - """
        api = API()
        client_id = value
        method = 'get_brands_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else "GET",
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking POST /brands')
    @allure.label('layer', 'api_tests')
    def test_api_post_brand(self):
        """ Checking POST /brands - """
        api = API()
        method = 'post_brands'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        body = {
            "name": name,
            "description": "123"
        }

        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking POST /brands [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('duplicate_name', 'Test brand1', 409),
            ('empty_body', '', 422),
            ('incorrect_method', 'PUT', 405),
            ('without_auth_token', '', 401),
            ('name_longer_than_256', '', 422)
        ]
    )
    def test_api_post_brand_negative(self, case: str, value: str, code: int):
        """ Checking POST /brands [negative] - """
        api = API()
        method = 'post_brands'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'name_longer_than_256':
            value = 'a' * 257
        if case == 'without_auth_token':
            headers = ''
        name = value
        body = '' if case == 'empty_body' else {
            "name": name,
            "description": "123"
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking PUT /brands/id')
    @allure.label('layer', 'api_tests')
    def test_api_put_brand_id(self, config):
        """ Checking PUT /brands/id - """
        api = API()
        method = 'get_brands_id'
        client_id = config.path_talks_data['client_id']['positive_5']
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        body = {
            "name": name,
            "description": "123"
        }

        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Brand')
    @allure.title('Checking PUT /brands/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('duplicate_name', 'Test brand', 409),
            ('empty_body', '', 422),
            ('incorrect_method', 'POST', 405),
            ('without_auth_token', '', 401),
            ('name_longer_than_256', '', 422)
        ]
    )
    def test_api_put_brand_id_negative(self, case: str, value: str, code: int, config):
        """ Checking PUT /brands/id [negative] - """
        api = API()
        method = 'get_brands_id'
        client_id = config.path_talks_data['client_id']['positive_5']
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'name_longer_than_256':
            value = 'a' * 257
        if case == 'without_auth_token':
            headers = ''
        name = value
        body = '' if case == 'empty_body' else {
            "name": name,
            "description": "123"
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking GET /clients/client_id/notification-urls [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_client_notification_url(self, case: str, value: str, config):
        """ Checking GET /clients/client_id/notification-urls - """
        api = API()
        method = 'get_client_notification_urls'
        client_id = config.path_talks_data['client_id']['positive_6']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking GET /clients/client_id/notification-urls [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
            ('incorrect_client_id', '1231233-7956-723a-ab5e-4593bca509f3', 404),
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401)

        ]
    )
    def test_api_get_client_notification_url_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking GET /clients/client_id/notification-urls [negative] - """
        api = API()
        method = 'get_client_notification_urls'
        client_id = value if case == 'incorrect_client_id' \
            else config.path_talks_data['client_id']['positive_6']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking GET /clients/client_id/notification-urls/id')
    @allure.label('layer', 'api_tests')
    def test_api_get_client_notification_url_id(self, config):
        """ Checking GET /clients/client_id/notification-urls/id - """
        api = API()
        id_url = config.path_talks_data['notification_id']['positive_1']
        client_id = config.path_talks_data['client_id']['positive_7']
        method = 'get_client_notification_urls_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            id=id_url, clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking GET /clients/client_id/notification-urls/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
            ('incorrect_client_id', '018f2d5e-7956-723a-ab5e-4593bca509f3', 404)
        ]
    )
    def test_api_get_client_notification_url_id_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking GET /clients/client_id/notification-urls/id [negative] - """
        api = API()
        id_url = config.path_talks_data['notification_id']['positive_1']
        client_id = value if case == 'incorrect_client_id' \
            else config.path_talks_data['client_id']['positive_6']
        method = 'get_client_notification_urls_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            id=id_url, clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking PUT /clients/client_id/notification-urls/id')
    @allure.label('layer', 'api_tests')
    def test_api_put_client_notification_url_id(self, config):
        """ Checking PUT /clients/client_id/notification-urls/id - """
        api = API()
        method = 'get_client_notification_urls'
        client_id = config.path_talks_data['client_id']['positive_8']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        signature_key = TestData.last_name()
        body = {
            "url": "https://checktest.com",
            "type": "smsOutgoing",
            "signatureKey": signature_key + "+323232"

        }

        res = api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )
        method = 'get_client_notification_urls_id'
        id_url = res.json().get('id')
        client_id = config.path_talks_data['client_id']['positive_8']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id, id=id_url)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        signature_key = TestData.last_name()
        body = {
            "url": "https://example.com",
            "type": "smsIncoming",
            "signatureKey": signature_key + "+232323"
        }
        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )
        body = {
            "url": "https://example.com",
            "type": "smsOutgoing",
            "signatureKey": signature_key + "+323232"
        }
        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )
        api.make_request(
            method_type='DELETE',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking PUT /clients/client_id/notification-urls/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('empty_body', '', 422),
            ('incorrect_method', 'POST', 405),
            ('without_auth_token', '', 401),
            ('name_longer_than_256', '', 422),
            ('signature_key_empty', '', 422)
        ]
    )
    def test_api_put_client_notification_url_id_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking PUT /clients/client_id/notification-urls/id [negative] - """
        api = API()
        method = 'get_client_notification_urls_id'
        id_url = config.path_talks_data['notification_id']['positive_2']
        client_id = config.path_talks_data['client_id']['positive_6']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id, id=id_url)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'name_longer_than_256':
            value = 'a' * 257
        if case == 'without_auth_token':
            headers = ''
        name = value
        signature_key = TestData.last_name()
        body = '' if case == 'empty_body' else {
            "name": name,
            "type": "smsOutgoing",
            "signatureKey": value if case == 'signature_key_empty' else signature_key + "+232323"
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking POST /clients/client_id/notification-urls')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case',
        [
                 "smsOutgoing",
                 "smsIncoming",
                 "email",
                 "litigationDnc",
                 "marketingDnc"
        ]
    )
    def test_api_post_client_notification_url(self, case: str, config):
        """ Checking POST /clients/client_id/notification-urls - """
        api = API()
        method = 'get_client_notification_urls'
        client_id = config.path_talks_data['client_id']['positive_8']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        signature_key = TestData.last_name()
        body = {
            "url": "https://checktest.com",
            "type": case,
            "signatureKey": signature_key + "+323232"

        }

        res = api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )
        method_delete = 'get_client_notification_urls_id'
        id_url = res.json().get('id')
        client_id = config.path_talks_data['client_id']['positive_8']
        url = API_URL + ENDPOINTS_MAPPING[method_delete].format(
            clientId=client_id, id=id_url)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='DELETE',
            url=url,
            method=method_delete,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Notification')
    @allure.title('Checking POST /clients/client_id/notification-urls [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('duplicate_name', 'smsIncoming', 409),
            ('empty_body', '', 422),
            ('incorrect_method', 'PUT', 405),
            ('without_auth_token', '', 401),
            ('name_longer_than_256', '', 422),
            ('signature_key_empty', '', 422)
        ]
    )
    def test_api_post_client_notification_url_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking POST /clients/client_id/notification-urls [negative] - """
        api = API()
        method = 'get_client_notification_urls'
        client_id = config.path_talks_data['client_id']['positive_8']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'name_longer_than_256':
            url_value = 'https://' + 'a' * 257 + '.com'
        else:
            url_value = 'https://name.com'
        if case == 'without_auth_token':
            headers = ''
        signature_key = TestData.last_name()
        body = '' if case == 'empty_body' else {
            "url": url_value,
            "type": value if case == 'duplicate_name' else "smsOutgoing",
            "signatureKey": value if case == 'signature_key_empty' else signature_key + "+232323"
        }
        if case == 'duplicate_name':

            res = api.make_request(
                method_type='POST',
                url=url,
                method=method,
                body=body,
                headers=headers,
                response_validator=False
            )

            api.make_request(
                method_type='POST',
                url=url,
                method=method,
                body=body,
                headers=headers,
                negative=True,
                expected_status_code=409,
                response_validator=False
            )
            method = 'get_client_notification_urls_id'
            id_url = res.json().get('id')
            delete_url = API_URL + ENDPOINTS_MAPPING[method].\
                format(clientId=client_id, id=id_url)
            api.make_request(
                method_type='DELETE',
                url=delete_url,
                method=method,
                headers=headers,
                response_validator=False
            )

    @allure.story('Path Talks Notification')
    @allure.title('Checking DELETE /clients/client_id/notification-urls/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_method', 'POST', 405),
            ('delete_inactive_notification', '0190c9ed-d3c4-71dc-beba-f362aeeb252d', 404),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_delete_client_notification_url_id_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking DELETE /clients/client_id/notification-urls/id [negative]- """
        api = API()
        method = 'get_client_notification_urls_id'
        id_url = config.path_talks_data['notification_id']['positive_3']
        client_id = config.path_talks_data['client_id']['positive_8']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id, id=id_url)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'DELETE',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking POST /clients/client_id/sms/channels [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('strategy_externalPhoneNumberPool', 'externalPoolId'),
           # ('strategy_phoneNumber', 'phoneFrom') #TODO need fix

        ]
    )
    def test_api_post_client_sms_channel(self, case: str, value: str, config):
        """ Checking POST /clients/client_id/sms/channels - """
        api = API()
        method = 'post_client_sms_channel'
        client_id = config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        external_pool_id = TestData().last_name()
        phone_from = TestData().zip_code()
        body = '' if case == 'empty_body' else {
            "accountId": '018f7b64-5057-734d-9899-6d2f77484e02',
            "name": name,
            "description": "test_desc",
            "strategy": "externalPhoneNumberPool"
            if case == 'strategy_externalPhoneNumberPool' else "phoneNumber",
            "settings": {
                "externalPoolId": external_pool_id
                if case == 'strategy_externalPhoneNumberPool' else None,
                "phoneFrom": "+194934" + phone_from
                if case != 'strategy_externalPhoneNumberPool' else None
            }
        }

        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking POST /clients/client_id/sms/channels [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('duplicate_name', 'Charlie', 409),
            ('empty_body', '', 422),
            ('incorrect_method', 'PUT', 405),
            ('without_auth_token', '', 401),

        ]
    )
    def test_api_post_client_sms_channel_negative(
            self,
            case: str,
            code: int,
            value: str,
            config
    ):
        """ Checking POST /clients/client_id/sms/channels [negative] - """
        api = API()
        method = 'post_client_sms_channel'
        client_id = config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        name = TestData().first_name()
        external_pool_id = TestData().last_name()
        phone_from = TestData().zip_code()
        body = '' if case == 'empty_body' else {
            "accountId": '018f7b64-5057-734d-9899-6d2f77484e02',
            "name": value if case == 'duplicate_name' else name,
            "description": "test desc",
            "strategy": "externalPhoneNumberPool"
            if case == 'strategy_externalPhoneNumberPool' else "phoneNumber",
            "settings": {
                "externalPoolId": external_pool_id
                if case == 'strategy_externalPhoneNumberPool' else None,
                "phoneFrom": "+194934" + phone_from
                if case != 'strategy_externalPhoneNumberPool' else None
            }
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking GET /clients/client_id/sms/channels [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_client_sms_channel(self, case: str, value: str, config):
        """ Checking GET /clients/client_id/sms/channels - """
        api = API()
        method = 'post_client_sms_channel'
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking GET /clients/client_id/sms/channels [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_account_id', '01241237f-23fe-7028-b331-b88eef13515', 404),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
        ]
    )
    def test_api_get_client_sms_channel_negative(
            self,
            case: str,
            code: int,
            value: str,
            config
    ):
        """ Checking GET /clients/client_id/sms/channels [negative] - """
        api = API()
        method = 'post_client_sms_channel'
        client_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking GET /clients/client_id/sms/channels/id')
    @allure.label('layer', 'api_tests')
    def test_api_get_client_sms_channel_id(self, config):
        """ Checking GET /clients/client_id/sms/channels/id - """
        api = API()
        method = 'get_client_sms_channel_id'
        channel_id = config.path_talks_data['channel_id']['positive_3']
        client_id = config.path_talks_data['client_id']['positive_4']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking GET /clients/client_id/sms/channels/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_account_id', '01241237f-23fe-7028-b331-b88eef13515', 404),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
        ]
    )
    def test_api_get_client_sms_channel_id_negative(
            self,
            case: str,
            code: int,
            value: str,
            config
    ):
        """ Checking GET /clients/client_id/sms/channels/id [negative] - """
        api = API()
        method = 'get_client_sms_channel_id'
        channel_id = config.path_talks_data['channel_id']['positive_3']
        client_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking PUT /clients/client_id/sms/channels/id/status [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('status_inactive', 'inactive'),
            ('status_active', 'active')
        ]
    )
    def test_api_put_client_sms_channel_id_status(self, case: str, value: str, config):
        """ Checking PUT /clients/client_id/sms/channels/id/status - """
        api = API()
        method = 'put_client_sms_channel_id_status'
        channel_id = config.path_talks_data['channel_id']['positive_4']
        client_id = config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {
            "status": value if case == 'status_inactive' else 'active'
        }

        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking PUT /clients/client_id/sms/channels/id/status [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
            ('status_active', 'actevi', 422)
        ]
    )
    def test_api_put_client_sms_channel_id_status_negative(
            self,
            case: str,
            code: int,
            value: str,
            config
    ):
        """ Checking PUT /clients/client_id/sms/channels/id/status [negative] - """
        api = API()
        method = 'put_client_sms_channel_id_status'
        channel_id = config.path_talks_data['channel_id']['positive_4']
        client_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = {
            "status": value
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking PUT /clients/client_id/sms/channels/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('strategy_externalPhoneNumberPool', 'externalPoolId'),
            ('strategy_phoneNumber', 'phoneFrom'),
            ('another_sms_account id', '018f7fc2-5d3a-73e4-a68c-e9d33ba66229')
        ]
    )
    def test_api_put_client_sms_channel_id(self, case: str, value: str, config):
        """ Checking PUT /clients/client_id/sms/channels/id - """
        api = API()
        method = 'get_client_sms_channel_id'
        channel_id = config.path_talks_data['channel_id']['positive_5']
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        name = TestData().first_name()
        external_pool_id = TestData().last_name()
        phone_from = TestData().zip_code()
        body = {
            "accountId": value if case == 'another_sms_account_id'
            else "018f7fb4-3cfa-710b-9341-42b4fa80161a",
            "name": name,
            "description": "test desc",
            "strategy": "externalPhoneNumberPool"
            if case == 'strategy_externalPhoneNumberPool' else "phoneNumber",
            "settings": {
                "externalPoolId": external_pool_id
                if case == 'strategy_externalPhoneNumberPool' else None,
                "phoneFrom": "+194934" + phone_from
                if case != 'strategy_externalPhoneNumberPool' else None
            }
        }

        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Channel')
    @allure.title('Checking PUT /clients/client_id/sms/channels/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('duplicate_name', 'Channel 1', 409),
            ('incorrect_method', 'POST', 405),
        ]
    )
    def test_api_put_client_sms_channel_id_negative(
            self,
            case: str,
            code: int,
            value: str,
            config
    ):
        """ Checking PUT /clients/client_id/sms/channels/id [negative] - """
        api = API()
        method = 'get_client_sms_channel_id'
        channel_id = config.path_talks_data['channel_id']['positive_1']
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        name = TestData().first_name()
        external_pool_id = TestData().last_name()
        phone_from = TestData().zip_code()
        body = {
            "accountId": "018f7fb4-3cfa-710b-9341-42b4fa80161a",
            "name": value if case == 'duplicate_name' else name,
            "description": "test_desc",
            "strategy": "externalPhoneNumberPool"
            if case == 'strategy_externalPhoneNumberPool' else "phoneNumber",
            "settings": {
                "externalPoolId": external_pool_id
                if case == 'strategy_externalPhoneNumberPool' else None,
                "phoneFrom": "+194934" + phone_from
                if case != 'strategy_externalPhoneNumberPool' else None
            }
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Compliance')
    @allure.title('Checking GET /compliance/litigation-dnc/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('phone_number_id', '01945fdf-f0cc-73a5-92ac-7ea9cd7b0474'),
            ('phone_number', '+155599981121')
        ]
    )
    def test_api_get_compliance_dns_id(
        self,
        case: str,
        value: str
    ):
        """ Checking GET /compliance/litigation-dnc/id - """
        api = API()
        method = 'get_compliance_litigation_dnc_id'
        phone_number = value
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(id=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Compliance')
    @allure.title('Checking GET /compliance/litigation-dnc/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_id', '018f7fb4-3cfa-710b-9341-42b4fa80161a', 404),
            ('phone_number_not_format_e164', '155599981121', 422),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_get_compliance_dns_id_negative(
        self,
        case: str,
        value: str,
        code: int
    ):
        """ Checking GET /compliance/litigation-dnc/id [negative] - """
        api = API()
        method = 'get_compliance_litigation_dnc_id'
        phone_number = value if case == 'incorrect_id' else '155599981121'
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(id=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Compliance')
    @allure.title('Checking POST /compliance/litigation-dnc')
    @allure.label('layer', 'api_tests')
    def test_api_post_compliance_dnc(self):
        """ Checking POST /compliance/litigation-dnc - """
        api = API()
        method = 'post_compliance_litigation_dnc'
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        phone_create = TestData().zip_code()
        body = {
                "phone": "+191313" + phone_create,
                "description": "Test number"
        }

        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Compliance')
    @allure.title('Checking POST /compliance/litigation-dnc [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('phone_number_not_format_e164', '155599981121', 422),
            ('duplicate_phone_number', '+155599981121', 409),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PATCH', 405)
        ]
    )
    def test_api_post_compliance_dnc_negative(
        self,
        case: str,
        value: str,
        code: int
    ):
        """ Checking POST /compliance/litigation-dnc [negative] - """
        api = API()
        method = 'post_compliance_litigation_dnc'
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = {
                "phone": value,
                "description": "Test number"
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Compliance')
    @allure.title('Checking DELETE /compliance/litigation-dnc/id')
    @allure.label('layer', 'api_tests')
    def test_api_delete_compliance_dnc(self):
        """ Checking DELETE /compliance/litigation-dnc/id - """
        api = API()
        method = 'post_compliance_litigation_dnc'
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        phone_create = TestData().zip_code()
        body = {
                "phone": "+191313" + phone_create,
                "description": "Test number"
        }

        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )
        new_number_phone = "+191313" + phone_create
        method = 'get_compliance_litigation_dnc_id'
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(id=new_number_phone)
        api.make_request(
            method_type='DELETE',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Compliance')
    @allure.title('Checking DELETE /compliance/litigation-dnc/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('not_real_phone_number', '+133322281111', 404),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_delete_compliance_dnc_negative(
        self,
        case: str,
        value: str,
        code: int
    ):
        """ Checking DELETE /compliance/litigation-dnc/id [negative] - """
        api = API()
        method = 'get_compliance_litigation_dnc_id'
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        phone_create = TestData.zip_code()
        new_number_phone = "+191313" + phone_create
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(id=new_number_phone)
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'DELETE',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/forbidden-words [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_forbidden_words(
            self,
            case: str,
            value: str
    ):
        """ Checking GET /sms/forbidden-words - """
        api = API()
        method = 'get_sms_forbidden_words'
        url = API_URL + ENDPOINTS_MAPPING[method].format()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_params':
            params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/forbidden-words [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_get_forbidden_words_negative(
            self,
            case: str,
            value: str,
            code: int,
    ):
        """ Checking GET /sms/forbidden-words [negative] - """
        api = API()
        method = 'get_sms_forbidden_words'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/forbidden-words/usage [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('negative_limit', '',)
        ]
    )
    def test_api_get_forbidden_words_usage(
            self,
            case: str,
            value: str,
    ):
        """ Checking GET /sms/forbidden-words/usage - """
        api = API()
        method = 'get_sms_forbidden_words'
        url = API_URL + ENDPOINTS_MAPPING[method].format()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = '' if case == 'without_params' else {'message': 'wolf, rabbit'}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/forbidden-words/usage [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_get_forbidden_words_usage_negative(
            self,
            case: str,
            value: str,
            code: int,
    ):
        """ Checking GET /sms/forbidden-words/usage [negative] - """
        api = API()
        method = 'get_sms_forbidden_words'
        url = API_URL + ENDPOINTS_MAPPING[method].format()
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        params = {'message': 'wolf, rabbit'}

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PUT /sms/forbidden-words')
    @allure.label('layer', 'api_tests')
    def test_api_put_forbidden_words(self, config):
        """ Checking PUT /sms/forbidden-words - """
        api = API()
        method = 'get_sms_forbidden_words'
        channel_id = config.path_talks_data['channel_id']['positive_1']
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = [
                "rabbit",
                "mobil",
                "car",
                "clear",
                "ruf",
                "checker"
        ]

        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PUT /sms/forbidden-words [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405),
        ]
    )
    def test_api_put_forbidden_words_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking PUT /sms/forbidden-words [negative] - """
        api = API()
        method = 'get_sms_forbidden_words'
        channel_id = config.path_talks_data['channel_id']['positive_1']
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = [
            "rabbit",
            "mobil",
            "car",
            "clear",
            "ruf",
            "checker"
        ]

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PATCH /sms/forbidden-words')
    @allure.label('layer', 'api_tests')
    def test_api_patch_forbidden_words(self, config):
        """ Checking PATCH /sms/forbidden-words - """
        api = API()
        method = 'get_sms_forbidden_words'
        channel_id = config.path_talks_data['channel_id']['positive_1']
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        forbidden_random = TestData.last_name()
        body = [
            forbidden_random,
            "rabbit",
            "mobil",
            "car",
            "clear",
            "ruf",
            "checker"
        ]

        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking PATCH /sms/forbidden-words [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_patch_forbidden_words_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking PATCH /sms/forbidden-words [negative] - """
        api = API()
        method = 'get_sms_forbidden_words'
        channel_id = config.path_talks_data['channel_id']['positive_1']
        client_id = config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, id=channel_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        forbidden_random = TestData.last_name()
        body = [
            forbidden_random
        ]

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking POST /sms [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('recipient_category_lead', 'lead'),
            ('recipient_category_client', 'client'),
            ('communication_category_marketing', 'marketing'),
            ('communication_category_transactional', 'transactional')
        ]
    )
    def test_api_post_test_send_sms_dummy(
            self,
            case: str,
            value: str,
            config
    ):
        """ Checking POST /sms - """
        api = API()
        method = 'post_test_send_sms_dummy'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN_DUMMY"]}'}
        phone_to = TestData.zip_code()
        body_sms = TestData.last_name()
        body = {
            "smsChannelId": config.path_talks_data['channel_id']['positive_2'],
            "phoneTo": "+194933" + phone_to,
            "body": body_sms,
            "recipientCategory": value if case == 'recipient_category_lead' else "client",
            "communicationCategory": value if case == 'communication_category_marketing'
            else "transactional",
            "timeZone": "Asia/Ho_Chi_Minh"
}

        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking POST /sms [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('send_sms_to_phone_dnc', '+19495367771', 422),
            ('incorrect_recipient_category', 'check', 422),
            ('incorrect_communication_category', 'kek', 422),
            ('incorrect_method', 'GET', 405),
            ('incorrect_timeZone', 'No/Here', 422)
        ]
    )
    def test_api_post_test_send_sms_dummy_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking POST /sms [negative] - """
        api = API()
        method = 'post_test_send_sms_dummy'
        url = API_URL + ENDPOINTS_MAPPING[method]
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN_DUMMY"]}'}
        if case == 'without_auth_token':
            headers = ''
        phone_to = TestData.zip_code()
        body_sms = TestData.last_name()
        body = {
            "smsChannelId": config.path_talks_data['channel_id']['positive_1'],
            "phoneTo": value if case == 'send_sms_to_phone_dnc' else "+194934" + phone_to,
            "body": body_sms,
            "recipientCategory": value if case == 'incorrect_recipient_category' else "client",
            "communicationCategory": value if case == 'incorrect_communication_category'
            else "transactional",
            "timeZone": value if case == 'incorrect_timeZone' else "Asia/Ho_Chi_Minh"
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking PUT /clients/client_id/recipient-phone/current_phone_number')
    @allure.label('layer', 'api_tests')
    def test_api_put_recipient_phone(self, config):
        """ Checking PUT /clients/client_id/recipient-phone/current_phone_number - """
        api = API()
        method = 'put_recipient_phone'
        phone_to = TestData.zip_code()
        current_phone = "+194934" + phone_to
        client_id = config.path_talks_data['client_id']['positive_9']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, currentPhoneNumber=current_phone)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {
                    "previousPhone": "+15559998877"
        }

        api.make_request(
            method_type='PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking PUT /clients/client_id/recipient-phone/current_phone_number [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('Duplicate_number', '15559998877', 422),
            ('incorrect_phone', '', 422),
            ('incorrect_method', 'GET', 405),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_put_recipient_phone_negative(
            self,
            case: str,
            value: str,
            code: int,
            config

    ):
        """ Checking PUT /clients/client_id/recipient-phone/current_phone_number [negative] - """
        api = API()
        method = 'put_recipient_phone'
        current_phone = value if case == 'Duplicate_number' else "194934"
        client_id = config.path_talks_data['client_id']['positive_9']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id, currentPhoneNumber=current_phone)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = {
                    "previousPhone":  "+15559998877"
        }

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'PUT',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/compliance/marketing-dnc-phone/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('phone_number_id', '01946924-0e86-7013-a4d6-481b9832ae4a'),
            ('phone_number', '+194953123123')
        ]
    )
    def test_api_get_marketing_dns_phone_id(
        self,
        case: str,
        value: str,
        config
    ):
        """ Checking GET /brands/brand_id/compliance/marketing-dnc-phone/id - """
        api = API()
        method = 'get_marketing_dnc_phone_id'
        phone_number = value if case == 'phone_number_id' else '+194953123123'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(brandId=brand_id, id= phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/compliance/marketing-dnc-phone/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_phone', '+11110011111', 404),
            ('incorrect_method', 'POST', 405),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_get_marketing_dns_phone_id_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking GET /brands/brand_id/compliance/marketing-dnc-phone/id [negative] - """
        api = API()
        method = 'get_marketing_dnc_phone_id'
        phone_number = value if case == 'incorrect_phone' else '+19495367771'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(brandId=brand_id, id=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking POST /brands/brand_id/compliance/marketing-dnc-phone [{case}]')
    @allure.label('layer', 'api_tests')
    def test_api_post_marketing_dns_phone(self, config):
        """ Checking POST /brands/brand_id/compliance/marketing-dnc-phone - """
        api = API()
        method = 'post_marketing_dnc_phone'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        phone_to = TestData.zip_code()
        body = {
                "phone": "+194934" + phone_to,
                "description": "test desc"
        }
        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking POST /brands/brand_id/compliance/marketing-dnc-phone [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_phone', '', 422),
            ('incorrect_method', 'PATCH', 405),
            ('duplicate_number', '+19495367771', 409),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_post_marketing_dns_phone_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking POST /brands/brand_id/compliance/marketing-dnc-phone [negative] - """
        api = API()
        method = 'post_marketing_dnc_phone'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = {
                "phone": value if case == 'incorrect_phone' else "+19495367771",
                "description": "test desc"
        }
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE /brands/brand_id/compliance/marketing-dnc-phone/id')
    @allure.label('layer', 'api_tests')
    def test_api_delete_marketing_dns_phone(self, config):
        """ Checking DELETE /brands/brand_id/compliance/marketing-dnc-phone/id - """
        api = API()
        method = 'get_marketing_dnc_phone_id'
        phone_number = '+19495367771'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id, id=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='DELETE',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

        api = API()
        method = 'post_marketing_dnc_phone'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        body = {
                "phone": "+19495367771",
                "description": "test desc"
        }
        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE /brands/brand_id/compliance/marketing-dnc-phone/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('not_real_phone_number', '+133322281111', 404),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_delete_marketing_dns_phone_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking DELETE /brands/brand_id/compliance/marketing-dnc-phone/id [negative] - """
        api = API()
        method = 'get_marketing_dnc_phone_id'
        phone_number = value if case == 'not_real_phone_number' else '19495367771'
        brand_id = config.path_talks_data['brand_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id, id=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'DELETE',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Email')
    @allure.title('Checking POST /clients/client_id/emails/accounts')
    @allure.label('layer', 'api_tests')
    def test_api_post_emails_accounts(self, config):
        """ Checking POST /clients/client_id/emails/accounts - """
        api = API()
        method = 'post_emails_account'
        client_id = config.path_talks_data['client_id']['positive_10']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}

        api.make_request(
            method_type='POST',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks Emails')
    @allure.title('Checking POST /clients/client_id/emails/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_client_id', '01802f85-5da7-71b9-b123-4567db4c0d6c', 404),
            ('incorrect_method', 'PATCH', 405),
            ('without_auth_token', '', 401)
        ]
    )
    def test_api_post_emails_accounts_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking POST /clients/client_id/emails/accounts [negative] - """
        api = API()
        method = 'post_emails_account'
        client_id = value if case == 'incorrect_client_id' \
            else config.path_talks_data['client_id']['positive_10']
        url = API_URL + ENDPOINTS_MAPPING[method]. \
            format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks Emails')
    @allure.title('Checking GET /clients/client_id/emails/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000),
            ('with_status', 'empty')
        ]
    )
    def test_api_get_emails_account(
            self,
            case: str,
            value: str,
            config
    ):
        """ Checking GET /clients/client_id/emails/accounts - """
        api = API()
        method = 'get_emails_account'
        client_id = config.path_talks_data['client_id']['positive_10']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_params':
            params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}
        if case == 'with_status':
            params = {'status': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /clients/client_id/emails/accounts [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PATCH', 405)
        ]
    )
    def test_api_get_emails_account_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking GET /clients/client_id/emails/accounts [negative] - """
        api = API()
        method = 'get_emails_account'
        client_id = config.path_talks_data['client_id']['positive_10']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    # @allure.story('Path Talks Emails')   @TODO need fix
    # @allure.title('Checking GET /clients/client_id/emails/accounts/id')
    # @allure.label('layer', 'api_tests')
    # def test_api_get_emails_account_id(self, config):
    #     """ Checking GET /clients/client_id/emails/accounts/id - """
    #     api = API()
    #     method = 'get_emails_account_id'
    #     client_id = config.path_talks_data['client_id']['positive_10']
    #     account_id = config.path_talks_data['account_sms_id']['positive_1']
    #     url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id, id=account_id)
    #     headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
    #     api.make_request(
    #         method_type='GET',
    #         url=url,
    #         method=method,
    #         headers=headers,
    #         response_validator=False
    #     )

    @allure.story('Path Talks Emails')
    @allure.title('Checking GET /clients/client_id/emails/accounts/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'POST', 405)
        ]
    )
    def test_api_get_emails_account_id_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking GET /clients/client_id/emails/accounts/id [negative] - """
        api = API()
        method = 'get_emails_account_id'
        client_id = config.path_talks_data['client_id']['positive_10']
        account_id = config.path_talks_data['account_sms_id']['positive_3']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id, id=account_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /clients/clientId/sms-outgoing [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, params',
        [
            ('without_params', {}),
            ('with_limit', {'limit': random.randint(1, 20)}),
            ('with_offset', {'offset': random.randint(1, 20)}),
            ('with_offset_and_limit', {'limit': random.randint(1, 20), 'offset': random.randint(1, 20)}),
            ('with_max_limit', {'limit': 1000}),
            ('with_max_offset', {'offset': 10000})
        ]
    )
    def test_api_sms_outgoing_list(self, case: str, params: dict, config):
        """Checking GET /clients/clientId/sms-outgoing """
        api = API()
        method = 'get_sms_outgoing_list'
        client_id = config.path_talks_data['client_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(
            clientId=client_id)
        headers= {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /clients/clientId/sms-outgoing [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('incorrect_account_id', '01241237f-23fe-7028-b331-b88eef13515', 404),
            ('without_auth_token', '', 401),
            ('access_denied', '', 403),
            ('incorrect_method', 'PUT', 405),
        ]
    )
    def test_api_sms_outgoing_list_negative(
            self,
            case: str,
            code: int,
            value: str,
            config
    ):
        """ Checking GET /clients/clientId/sms-outgoing [negative] - """
        api = API()
        method = 'get_sms_outgoing_list'
        client_id = value if case == 'incorrect_account_id' \
            else config.path_talks_data['client_id']['positive_main']
        url = API_URL + ENDPOINTS_MAPPING[method].format(clientId=client_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        if case == 'access_denied':
            headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN_NO_ACCESS"]}'}
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/outgoing/id')
    @allure.label('layer', 'api_tests')
    def test_api_get_sms_outgoing_id(self, config):
        """Checking GET /sms/outgoing/id - """
        api = API()
        id_sms = config.path_talks_data['sms_id']['positive_1']
        method = 'get_sms_outgoing_id'
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=id_sms)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks SMS')
    @allure.title('Checking GET /sms/outgoing/id [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('access_denied', '', 403),
            ('incorrect_method', 'POST', 405),
            ('incorrect_id', '018f2d5e-7956-723a-ab5e-4593bca509f3', 404)

        ]
    )
    def test_api_get_sms_outgoing_id_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """Checking GET /sms/outgoing/id [negative] - """
        api = API()
        method = 'get_sms_outgoing_id'
        id_sms = value if case == 'incorrect_id' \
            else config.path_talks_data['sms_id']['positive_1']
        url = API_URL + ENDPOINTS_MAPPING[method].format(id=id_sms)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        if case == 'access_denied':
            headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN_NO_ACCESS"]}'}
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    # @allure.story('Path Talks')   #TODO need fix
    # @allure.title('Checking GET /brands/brand_id/tcpa-consent/phone_number')
    # @allure.label('layer', 'api_tests')
    # def test_api_get_tcpa_consent_phone_number(self, config):
    #     """ Checking GET /brands/brand_id/tcpa-consent/phone_number - """
    #     api = API()
    #     method = 'get_tcpa_consent_phone_number'
    #     brand_id = config.path_talks_data['brand_id']['positive_3']
    #     phone_number = '+19434555331'
    #     url = API_URL + ENDPOINTS_MAPPING[method].\
    #         format(brandId=brand_id, phoneNumber=phone_number)
    #     headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
    #     api.make_request(
    #         method_type='GET',
    #         url=url,
    #         method=method,
    #         headers=headers,
    #         response_validator=False
    #     )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/tcpa-consent/phone_number [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('phone_dont_have_tcpa', '+19434222333', 404),
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PATCH', 405)
        ]
    )
    def test_api_get_tcpa_consent_phone_number_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking GET /brands/brand_id/tcpa-consent/phone_number [negative] - """
        api = API()
        method = 'get_tcpa_consent_phone_number'
        brand_id = config.path_talks_data['brand_id']['positive_3']
        phone_number = value if case == 'phone_dont_have_tcpa' else '+19434555331'
        url = API_URL + ENDPOINTS_MAPPING[method].\
            format(brandId=brand_id, phoneNumber=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/tcpa-consent/phone_number/history')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('phone_dont_have_tcpa_history', '+19434222333'),
            ('phone_with_tcpa_history', '+19434555331',)

        ]
    )
    def test_api_get_tcpa_consent_phone_number_history(
            self,
            case: str,
            value: str,
            config
    ):
        """ Checking GET /brands/brand_id/tcpa-consent/phone_number/history - """
        api = API()
        method = 'get_tcpa_consent_phone_number_history'
        brand_id = config.path_talks_data['brand_id']['positive_3']

        phone_number = value
        url = API_URL + ENDPOINTS_MAPPING[method].\
            format(brandId=brand_id, phoneNumber=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/tcpa-consent/phone_number/history [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PATCH', 405)
        ]
    )
    def test_api_get_tcpa_consent_phone_number_history_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking GET /brands/brand_id/tcpa-consent/phone_number/history [negative] - """
        api = API()
        method = 'get_tcpa_consent_phone_number_history'
        brand_id = config.path_talks_data['brand_id']['positive_3']
        phone_number = value if case == 'phone_dont_have_tcpa' else '+19434555331'
        url = API_URL + ENDPOINTS_MAPPING[method].\
            format(brandId=brand_id, phoneNumber=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    # @allure.story('Path Talks')   #TODO need fix
    # @allure.title('Checking POST /brands/brand_id/tcpa-consent/phone_number')
    # @allure.label('layer', 'api_tests')
    # def test_api_post_tcpa_consent_phone_number(self, config):
    #     """ Checking POST /brands/brand_id/tcpa-consent/phone_number - """
    #     api = API()
    #     method = 'get_tcpa_consent_phone_number'
    #     brand_id = config.path_talks_data['brand_id']['positive_3']
    #     phone_number = '+19433332333'
    #     url = API_URL + ENDPOINTS_MAPPING[method].\
    #         format(brandId=brand_id, phoneNumber=phone_number)
    #     headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
    #     body = {
    #             "expiresAt": "2025-03-15T05:10:00+00:00",
    #             "description": "Lead agreed TCPA consent via americor.com",
    #             "confirmationUrl": "https://cert.trustedform.com/AAABBBCCC111222333444555666777"
    #     }
    #     api.make_request(
    #         method_type='POST',
    #         url=url,
    #         method=method,
    #         body=body,
    #         headers=headers,
    #         response_validator=False
    #     )

    @allure.story('Path Talks')
    @allure.title('Checking POST /brands/brand_id/tcpa-consent/phone_number [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PATCH', 405)
        ]
    )
    def test_api_post_tcpa_consent_phone_number_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking POST /brands/brand_id/tcpa-consent/phone_number [negative]- """
        api = API()
        method = 'get_tcpa_consent_phone_number'
        brand_id = config.path_talks_data['brand_id']['positive_3']
        phone_number = '+19433332333'
        url = API_URL + ENDPOINTS_MAPPING[method].\
            format(brandId=brand_id, phoneNumber=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        body = {
                "expiresAt": "2025-03-15T05:10:00+00:00",
                "description": "Lead agreed TCPA consent via americor.com",
                "confirmationUrl": "https://cert.trustedform.com/AAABBBCCC111222333444555666777"
        }
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'POST',
            url=url,
            method=method,
            body=body,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    # @allure.story('Path Talks')   #TODO need fix
    # @allure.title('Checking DELETE /brands/brand_id/tcpa-consent/phone_number')
    # @allure.label('layer', 'api_tests')
    # def test_api_delete_tcpa_consent_phone_number(self, config):
    #     """ Checking DELETE /brands/brand_id/tcpa-consent/phone_number - """
    #     api = API()
    #     method = 'get_tcpa_consent_phone_number'
    #     brand_id = config.path_talks_data['brand_id']['positive_3']
    #     phone_number = '+19433332333'
    #     url = API_URL + ENDPOINTS_MAPPING[method].\
    #         format(brandId=brand_id, phoneNumber=phone_number)
    #     headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
    #     api.make_request(
    #         method_type='DELETE',
    #         url=url,
    #         method=method,
    #         headers=headers,
    #         response_validator=False
    #     )

    @allure.story('Path Talks')
    @allure.title('Checking DELETE /brands/brand_id/tcpa-consent/phone_number [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PATCH', 405)
        ]
    )
    def test_api_delete_tcpa_consent_phone_number_negative(
        self,
        case: str,
        value: str,
        code: int,
        config
    ):
        """ Checking DELETE /brands/brand_id/tcpa-consent/phone_number [negative]- """
        api = API()
        method = 'get_tcpa_consent_phone_number'
        brand_id = config.path_talks_data['brand_id']['positive_3']
        phone_number = '+19433332333'
        url = API_URL + ENDPOINTS_MAPPING[method].\
            format(brandId=brand_id, phoneNumber=phone_number)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        if case == 'without_auth_token':
            headers = ''
        api.make_request(
            method_type=value if case == 'incorrect_method' else 'DELETE',
            url=url,
            method=method,
            headers=headers,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/tcpa-consents [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value',
        [
            ('without_params', ''),
            ('with_limit', ''),
            ('with_offset', ''),
            ('with_offset_and_limit', ''),
            ('with_max_limit', '1000'),
            ('with_max_offset', 10000)
        ]
    )
    def test_api_get_brand_id_tcpa_consents(
            self,
            case: str,
            value: str,
            config
    ):
        """ Checking GET /brands/brand_id/tcpa-consents - """
        api = API()
        method = 'get_brands_id_tcpa_consents'
        brand_id = config.path_talks_data['brand_id']['positive_4']
        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''
        limit = random.randint(1, 20)
        offset = random.randint(1, 10)

        if case == 'with_limit':
            params = {'limit': limit}
        if case == 'with_offset':
            params = {'offset': offset}
        if case == 'with_offset_and_limit':
            params = {'limit': limit, 'offset': offset}
        if case == 'with_max_limit':
            params = {'limit': value}
        if case == 'with_max_offset':
            params = {'offset': value}

        api.make_request(
            method_type='GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            response_validator=False
        )

    @allure.story('Path Talks')
    @allure.title('Checking GET /brands/brand_id/tcpa-consents [{case}]')
    @allure.label('layer', 'api_tests')
    @pytest.mark.parametrize(
        'case, value, code',
        [
            ('without_auth_token', '', 401),
            ('incorrect_method', 'PUT', 405),
            ('incorrect_brand_id', '1231233-7956-723a-ab5e-4593bca509f3', 404),
            ('negative_offset', -1, 400),
            ('negative_limit', -1, 400),
            ('limit_zero', 0, 400),
            ('without_auth_token', '', 401)

        ]
    )
    def test_api_get_brand_id_tcpa_consents_negative(
            self,
            case: str,
            value: str,
            code: int,
            config
    ):
        """ Checking GET /brands/brand_id/tcpa-consents [negative] - """
        api = API()
        method = 'get_brands_id_tcpa_consents'
        brand_id = value if case == 'incorrect_brand_id' \
            else config.path_talks_data['brand_id']['positive_4']

        url = API_URL + ENDPOINTS_MAPPING[method].format(brandId=brand_id)
        headers = {'Authorization': f'Bearer {os.environ["PATH_TALKS_TOKEN"]}'}
        params = ''

        if case == 'negative_offset':
            params = {'offset': value}
        if case in ['negative_limit', 'limit_zero']:
            params = {'limit': value}
        if case == 'without_auth_token':
            headers = ''

        api.make_request(
            method_type=value if case == 'incorrect_method' else 'GET',
            url=url,
            method=method,
            headers=headers,
            params=params,
            negative=True,
            expected_status_code=code,
            response_validator=False
        )

    # функция для проверки коннекта к Slack
    # def test_slack_connection(self):
    #     from autotests.pages.utils import slack_post_msg
    #     slack_post_msg(
    #         token=os.environ['PERFORMANCE_BOT_TOKEN'],
    #         channel=os.environ.get('TEST_PATH_TALKS_RESULT_CHANNEL', '#qa_test_api_pathtalks_results'),
    #         text="Connection test: OK",
    #         username="Selenium"
    #     )
    #     assert True