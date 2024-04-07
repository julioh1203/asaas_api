import httpx

from asaas import Asaas


class AsaasCustomer(Asaas):
    """Asaas Customer Class"""

    def create_customer(self):
        """Create Customer"""
        url = self.api_url + "/customers"
        response = httpx.post(url, headers=self.headers)
        return response

    def get_customer(self, field_search, customer_cpf_cnpj):
        """Get Customer by CPF/CNPJ"""
        url = self.api_url + f"/customers?{field_search}={customer_cpf_cnpj}"
        response = httpx.get(url, headers=self.headers)
        return response
