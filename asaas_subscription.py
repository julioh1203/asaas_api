from asaas import Asaas


class AsaasSubscription(Asaas):
    """Asaas Subscription Class"""

    def create_subscription(self, payload):
        """Create Subscription"""
        url = self.api_url + "/subscriptions"
        return self.act_post_put("POST", url, payload)

    def list_subscription(self, field_search, parameters):
        """List Subscription"""
        url = self.api_url + f"/subscriptions?{field_search}={parameters}"
        return self.act_get_delete("GET", url)

    def get_subscription(self, subscription_id):
        """Get Subscription using ID"""
        url = self.api_url + f"/subscriptions/{subscription_id}"
        return self.act_get_delete("GET", url)

    def update_subscription(self, subscription_id, payload):
        """Update Subscription"""
        url = self.api_url + f"/subscriptions/{subscription_id}"
        return self.act_post_put("PUT", url, payload)

    def delete_subscription(self, subscription_id):
        """Delete Subscription"""
        url = self.api_url + f"/subscriptions/{subscription_id}"
        return self.act_get_delete("DELETE", url)

    def list_subscription_charging(self, subscription_id):
        """List Subscription Charging"""
        url = self.api_url + f"/subscriptions/{subscription_id}/payments"
        return self.act_get_delete("GET", url)

    def create_subscription_payment_book(self, subscription_id, month, year):
        """Create Subscription Payment Book"""
        url = (
            self.api_url
            + f"/subscriptions/{subscription_id}/paymentBook?month={month}&year={year}"
        )
        return self.act_get_delete("GET", url)
