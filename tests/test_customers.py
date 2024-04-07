def test_get_customer_by_cpf_cnpj(asaas_customer_instance):
    """Test Get Customer by CPF/CNPJ"""
    asaas = asaas_customer_instance
    response = asaas.get_customer("cpfCnpj", "12345678901")
    assert response.status_code == 200
