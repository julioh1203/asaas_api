import os

import pytest

from asaas_customers import AsaasCustomer


@pytest.fixture(scope="session")
def load_env_vars():
    return {
        "api_token": os.getenv("ASAAS_API_KEY"),
        "api_url": os.getenv("ASAAS_API_URL"),
    }


@pytest.fixture
def asaas_customer_instance(load_env_vars):
    asaas = AsaasCustomer(load_env_vars.get("api_token"), load_env_vars.get("api_url"))
    return asaas
