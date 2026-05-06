import requests


def test_viacep_api_returns_address():
    response = requests.get("https://viacep.com.br/ws/01001000/json/")

    assert response.status_code == 200

    data = response.json()

    assert "logradouro" in data
    assert "bairro" in data
    assert "localidade" in data
    assert "uf" in data
    assert data["localidade"] == "São Paulo"
    assert data["uf"] == "SP"