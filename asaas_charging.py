from asaas import Asaas


class AsaasCharging(Asaas):
    """Asaas Charging Class"""

    def create_charging(self, payload):
        """Create Charge"""
        url = self.api_url + "/payments"
        return self.act_post_put("POST", url, payload)

    def update_charging(self, charging_id, payload):
        """Update Charge"""
        url = self.api_url + f"/payments/{charging_id}"
        return self.act_post_put("PUT", url, payload)

    def delete_charging(self, charging_id):
        """Delete Charge"""
        url = self.api_url + f"/payments/{charging_id}"
        return self.act_get_delete("DELETE", url)

    def restore_charging(self, charging_id):
        """Restore Charge"""
        url = self.api_url + f"/payments/{charging_id}/restore"
        return self.act_post_put("POST", url)

    def get_charging_status(self, charging_id):
        """Get Charge Status"""
        url = self.api_url + f"/payments/{charging_id}/status"
        return self.act_get_delete("GET", url)

    def refund_charging(self, charging_id, payload):
        """Refund Charge"""
        url = self.api_url + f"/payments/{charging_id}/refund"
        return self.act_post_put("POST", url, payload)

    def get_code(self, charging_id):
        """Get Charge Code"""
        url = self.api_url + f"/payments/{charging_id}/identificationField"
        return self.act_get_delete("GET", url)

    def get_pix_qr_code(self, charging_id):
        """Get PIX QR Code"""
        url = self.api_url + f"/payments/{charging_id}/pixQrCode"
        return self.act_get_delete("GET", url)

    def inform_cash_payment(self, charging_id, payload):
        """
        Inform Cash Payment
        payload = {
            "paymentDate": "2024-04-10",
            "value": 100,
            "notifyCustomer": False
        }
        """
        url = self.api_url + f"/payments/{charging_id}/receiveInCash"
        return self.act_post_put("POST", url, payload)

    def undo_cash_payment(self, charging_id):
        """Undo Cash Payment"""
        url = self.api_url + f"/payments/{charging_id}/undoReceivedInCash"
        return self.act_post_put("POST", url)
