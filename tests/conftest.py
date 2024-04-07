import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def load_env_vars():
    return {
        "api_token": os.getenv("ASAAS_API_KEY"),
        "api_url": os.getenv("ASAAS_API_URL"),
    }
