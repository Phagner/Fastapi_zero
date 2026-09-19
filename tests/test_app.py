from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World!'}  # Asset


def teste_da_regra_do_primeiro_codigo():
    client = TestClient(app)

    response = client.get('/first_code')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1> Olá Mundo <h1>'
