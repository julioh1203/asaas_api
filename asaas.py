import os

import httpx


class Asaas:
    """Asaas Class"""

    def __init__(self):
        """Constructor"""
        self.api_key = os.getenv("ASAAS_API_KEY")
        self.api_url = os.getenv("ASAAS_API_URL")
        self.headers = {
            "accept": "application/json",
            "access_token": self.api_key,
        }

    def get_json(self, response):
        """Get JSON from response"""
        return response.json()

    def act_post_put(self, method, url, payload=None):
        """Act POST or PUT"""
        response = None
        if method == "POST":
            response = httpx.post(url, headers=self.headers, json=payload)
        elif method == "PUT":
            response = httpx.put(url, headers=self.headers, json=payload)
        return response

    def act_get_delete(self, method, url):
        """Act GET or DELETE"""
        response = None
        if method == "GET":
            response = httpx.get(url, headers=self.headers)
        elif method == "DELETE":
            response = httpx.delete(url, headers=self.headers)
        return response
