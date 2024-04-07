import os

from asaas import AsaasCustomer


def test_get_customer_by_cpf_cnpj(load_env_vars):
    """Test Get Customer by CPF/CNPJ"""

    asaas = AsaasCustomer(load_env_vars.get("api_token"), load_env_vars.get("api_url"))
    response = asaas.get_customer_by_cpf_cnpj("12345678901")
    assert response.status_code == 200
