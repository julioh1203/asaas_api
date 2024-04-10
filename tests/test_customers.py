import pytest


@pytest.mark.order(1)
def test_create_customer(asaas_customer_instance):
    """Test Create Customer"""
    payload = {
        "name": "John Doe",
        "email": "john.doe@asaas.com.br",
        "phone": "4738010919",
        "mobilePhone": "4799376637",
        "cpfCnpj": "24971563792",
        "postalCode": "01310-000",
        "address": "Av. Paulista",
        "addressNumber": "150",
        "complement": "Sala 201",
        "province": "Centro",
        "externalReference": "12987382",
        "notificationDisabled": False,
        "additionalEmails": "john.doe@asaas.com,john.doe.silva@asaas.com.br",
        "municipalInscription": "46683695908",
        "stateInscription": "646681195275",
        "observations": "ótimo pagador, nenhum problema até o momento",
    }
    asaas = asaas_customer_instance
    response = asaas.create_customer(payload)
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_customer_by_cpf_cnpj(asaas_customer_instance):
    """Test Get Customer by CPF/CNPJ"""
    asaas = asaas_customer_instance
    response = asaas.get_customer("cpfCnpj", "12345678901")
    assert response.status_code == 200


@pytest.mark.order(3)
def test_get_customer_by_id(asaas_customer_instance):
    """Test Get Customer by ID"""
    asaas = asaas_customer_instance
    response = asaas.get_customer_by_id("cus_000005958001")
    assert response.status_code == 200


@pytest.mark.order(4)
def test_update_customer(asaas_customer_instance):
    """Test Update Customer"""
    payload = {
        "address": "Av. Moema",
        "addressNumber": "23",
        "complement": "Sala 200",
        "province": "Moema",
    }
    asaas = asaas_customer_instance
    response = asaas.update_customer("cus_000005958001", payload)
    assert response.status_code == 200
    assert response.json()["address"] == "Av. Moema"


@pytest.mark.order(5)
def test_delete_customer(asaas_customer_instance):
    """Test Delete Customer"""
    asaas = asaas_customer_instance
    response = asaas.delete_customer("cus_000005958001")
    assert response.status_code == 200


@pytest.mark.order(6)
def test_restore_customer(asaas_customer_instance):
    """Test Recover Customer"""
    asaas = asaas_customer_instance
    response = asaas.restore_customer("cus_000005958001")
    assert response.status_code == 200


@pytest.mark.order(7)
def test_restore_customer_notifications(asaas_customer_instance):
    """Test Recover Customer Notifications"""
    asaas = asaas_customer_instance
    response = asaas.restore_customer_notifications("cus_000005958001")
    assert response.status_code == 200
