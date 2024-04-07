import httpx


class Asaas:
    """Asaas Class"""

    def __init__(self, api_key, api_url):
        """Constructor"""
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "access_token": self.api_key,
        }

    def get_json(self, response):
        return response.json()


class AsaasCustomer(Asaas):
    """Asaas Customer Class"""

    def create_customer(self):
        url = self.api_url + "/customers"
        response = httpx.post(url, headers=self.headers)
        return response

    def get_customer_by_cpf_cnpj(self, customer_cpf_cnpj):
        """Get Customer by CPF/CNPJ"""
        url = self.api_url + f"/customers?cpfCnpj={customer_cpf_cnpj}"
        response = httpx.get(url, headers=self.headers)
        return response
