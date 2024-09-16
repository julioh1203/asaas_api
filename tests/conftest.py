import os

import pytest

from asaas_charging import AsaasCharging
from asaas_customers import AsaasCustomer
from asaas_subscription import AsaasSubscription


@pytest.fixture(scope="session")
def load_env_vars():
    return {
        "api_token": os.getenv("ASAAS_API_KEY"),
        "api_url": os.getenv("ASAAS_API_URL"),
    }


@pytest.fixture
def asaas_customer_instance(load_env_vars):
    asaas = AsaasCustomer()
    return asaas


@pytest.fixture
def asaas_charging_instance(load_env_vars):
    asaas = AsaasCharging()
    return asaas


@pytest.fixture
def asaas_subscription_instance(load_env_vars):
    asaas = AsaasSubscription()
    return asaas
