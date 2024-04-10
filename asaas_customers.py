from asaas import Asaas


class AsaasCustomer(Asaas):
    """Asaas Customer Class"""

    def create_customer(self, payload):
        """Create Customer"""
        url = self.api_url + "/customers"
        return self.act_post_put("POST", url, payload)

    def get_customer(self, field_search, customer_cpf_cnpj):
        """Get Customer by CPF/CNPJ"""
        url = self.api_url + f"/customers?{field_search}={customer_cpf_cnpj}"
        return self.act_get_delete("GET", url)

    def get_customer_by_id(self, customer_id):
        """Get Customer by ID"""
        url = self.api_url + f"/customers/{customer_id}"
        return self.act_get_delete("GET", url)

    def update_customer(self, customer_id, payload):
        """Update Customer"""
        url = self.api_url + f"/customers/{customer_id}"
        return self.act_post_put("PUT", url, payload)

    def delete_customer(self, customer_id):
        """Delete Customer"""
        url = self.api_url + f"/customers/{customer_id}"
        return self.act_get_delete("DELETE", url)

    def restore_customer(self, customer_id):
        """Recover Customer"""
        url = self.api_url + f"/customers/{customer_id}/restore"
        return self.act_post_put("POST", url)

    def restore_customer_notifications(self, customer_id):
        """Recover Customer Notifications"""
        url = self.api_url + f"/customers/{customer_id}/notifications"
        return self.act_get_delete("GET", url)
