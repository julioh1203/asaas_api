import pytest


@pytest.fixture()
def test_create_charging(asaas_charging_instance):
    """Test Create Charging"""
    payload = {
        "billingType": "BOLETO",
        "interest": {"value": 1},
        "fine": {"value": 2, "type": "PERCENTAGE"},
        "customer": "cus_000005958001",
        "value": 100,
        "dueDate": "2024-06-30",
        "description": "Pedido 200",
        "installmentCount": 2,
        "totalValue": 100,
        "postalService": False,
    }
    asaas = asaas_charging_instance
    response = asaas.create_charging(payload)
    assert response.status_code == 200
    return response.json()["id"]


def test_update_charging(asaas_charging_instance, test_create_charging):
    """Test Get Charging"""
    payload = {
        "billingType": "BOLETO",
        "interest": {"value": 1},
        "fine": {"value": 2, "type": "PERCENTAGE"},
        "customer": "cus_000005958001",
        "value": 300,
        "dueDate": "2024-06-30",
        "description": "Pedido 200",
        "installmentCount": 2,
        "totalValue": 300,
        "postalService": False,
    }
    asaas = asaas_charging_instance
    response = asaas.update_charging(test_create_charging, payload)
    assert response.status_code == 200


def test_delete_charging(asaas_charging_instance, test_create_charging):
    """Test Delete Charging"""
    asaas = asaas_charging_instance
    response = asaas.delete_charging(test_create_charging)
    assert response.status_code == 200


def test_restore_charging(asaas_charging_instance, test_create_charging):
    """Test Restore Charging"""
    asaas = asaas_charging_instance
    asaas.delete_charging(test_create_charging)
    response = asaas.restore_charging(test_create_charging)
    assert response.status_code == 200


def test_get_charging_status(asaas_charging_instance, test_create_charging):
    """Test Get Charging Status"""
    asaas = asaas_charging_instance
    response = asaas.get_charging_status(test_create_charging)
    assert response.status_code == 200
    assert response.json()["status"] == "PENDING"


def test_refund_charging(asaas_charging_instance):
    """Test Refund Charging"""
    asaas = asaas_charging_instance
    payload_create_charging = {
        "billingType": "PIX",
        "interest": {"value": 1},
        "fine": {"value": 2, "type": "PERCENTAGE"},
        "customer": "cus_000005958001",
        "value": 100,
        "dueDate": "2024-06-30",
        "description": "Pedido 200",
        "installmentCount": 1,
        "totalValue": 100,
        "postalService": False,
    }
    response = asaas.create_charging(payload_create_charging)
    chargind_id = response.json()["id"]

    payload = {"value": 100, "description": "Test Refund"}
    response = asaas.refund_charging(chargind_id, payload)

    assert response.status_code == 400


def test_get_code(asaas_charging_instance, test_create_charging):
    """Test Get Code"""
    asaas = asaas_charging_instance
    response = asaas.get_code(test_create_charging)
    assert response.status_code == 200
    assert response.json()["barCode"] is not None


def test_get_pix_qr_code(asaas_charging_instance):
    """Test Get PIX QR Code"""
    asaas = asaas_charging_instance
    payload_create_charging = {
        "billingType": "PIX",
        "interest": {"value": 1},
        "fine": {"value": 2, "type": "PERCENTAGE"},
        "customer": "cus_000005958001",
        "value": 100,
        "dueDate": "2024-06-30",
        "description": "Pedido 200",
        "installmentCount": 1,
        "totalValue": 100,
        "postalService": False,
    }
    response = asaas.create_charging(payload_create_charging)
    chargind_id = response.json()["id"]
    response = asaas.get_pix_qr_code(chargind_id)
    assert response.status_code == 200
    assert response.json()["encodedImage"] is not None
