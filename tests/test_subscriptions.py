def test_create_subscription(asaas_subscription_instance):
    """Test Create Subscription"""
    payload = {
        "customer": "cus_000006210572",
        "billingType": "BOLETO",
        "installmentCount": 2,
        "cycle": "MONTHLY",
        "value": 100,
        "dueDate": "2024-06-30",
        "description": "Pedido 200",
        "postalService": False,
        "interest": {"value": 1},
        "fine": {"value": 2, "type": "PERCENTAGE"},
    }
    asaas = asaas_subscription_instance
    response = asaas.create_subscription(payload)
    assert response.status_code == 200
    return response.json()["id"]


def test_list_subscription(asaas_subscription_instance):
    """Test List Subscription"""
    asaas = asaas_subscription_instance
    response = asaas.list_subscription("customer", "cus_000005958001")
    assert response.status_code == 200


def test_get_subscription(asaas_subscription_instance):
    """Test Get Subscription"""
    asaas = asaas_subscription_instance
    subscription_id = test_create_subscription(asaas)
    response = asaas.get_subscription(subscription_id)
    assert response.status_code == 200
    assert response.json()["id"] == subscription_id


def test_update_subscription(asaas_subscription_instance):
    """Test Update Subscription"""
    asaas = asaas_subscription_instance
    subscription_id = test_create_subscription(asaas)
    payload = {
        "customer": "cus_000006210572",
        "billingType": "CREDIT_CARD",
        "installmentCount": 3,
        "cycle": "MONTHLY",
        "value": 300,
        "dueDate": "2024-06-30",
        "description": "Pedido 200",
        "postalService": False,
        "interest": {"value": 1},
        "fine": {"value": 2, "type": "PERCENTAGE"},
    }
    response = asaas.update_subscription(subscription_id, payload)
    assert response.status_code == 200
    assert response.json()["id"] == subscription_id
    assert response.json()["value"] == 300.0


def test_list_subscription_charging(asaas_subscription_instance):
    """Test List Subscription Charging"""
    asaas = asaas_subscription_instance
    subscription_id = test_create_subscription(asaas)
    response = asaas.list_subscription_charging(subscription_id)
    assert response.status_code == 200


def test_delete_subscription(asaas_subscription_instance):
    """Test Delete Subscription"""
    asaas = asaas_subscription_instance
    subscription_id = test_create_subscription(asaas)
    response = asaas.delete_subscription(subscription_id)
    assert response.status_code == 200
