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
        """Get JSON from response"""
        return response.json()
