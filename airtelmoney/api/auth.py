import requests
from requests.auth import HTTPBasicAuth
import json

class AirtelMoneyBase:
    
    def __init__(
        self, 
        env="sandbox",
        client_id=None, 
        client_secret=None,
        sandbox_url="https://openapiuat.airtel.africa/",
        live_url="https://openapi.airtel.africa/",
        ):
        self.env = env
        self.client_id = client_id
        self.client_secret = client_secret
        self.sandbox_url = sandbox_url
        self.live_url=live_url
        self.token = None


    def authenticate(self):

        """To make Airtel money API calls, you will need to authenticate your app. This method is used to fetch the access token
        required by  Airtel money.  Airtel money supports client_credentials grant type. To authorize your API calls to  Airtel money,
        you will need a Basic Auth over HTTPS authorization token. The Basic Auth string is a base64 encoded string
        of your app's client key and client secret.
            **Args:**
                - `env` (str): Current app environment. Options: sandbox, live.
                - `client_id` (str): The client id obtained from the developer portal.
                - `client_secret` (str): The client secret key obtained from the developer portal.
                - `sandbox_url` (str): Base Airtel Money UAT url.
                - `live_url` (str): Base Airtel Money live url.
            **Returns:**
                - `access_token` (str): This token is to be used with the Bearer header for further API calls to  Airtel money."""
        if self.env == "production":
            base_am_url = self.live_url
        else:
            base_am_url = self.sandbox_url

        authenticate_url  = f"{base_am_url}auth/oauth2/token"
        payload = json.dumps({
        "client_id":  self.client_id,
        "client_secret": self.client_secret,
        "grant_type": "client_credentials"
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", authenticate_url, headers=headers, data=payload)
        try:
            response = json.loads(response.text)
            access_token = response.get('access_token', None)
            if access_token:
                self.token = access_token
        except:
            pass

        return self.token