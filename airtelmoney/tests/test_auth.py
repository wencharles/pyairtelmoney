import  unittest
from airtelmoney.api import AirtelMoneyBase

class AuthTests(unittest.TestCase):
    def setUp(self):
        airtel_money_auth_obj = AirtelMoneyBase(
            env="sandbox", 
            client_id=None, 
            client_secret=None,
        )
        self.token = airtel_money_auth_obj.authenticate()

    
    def test_authenticate_token(self):
        self.assertEqual(len(self.token), 28)
