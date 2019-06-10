from django.test import TestCase
import json
# Create your tests here.


class AuthAdminTest(TestCase):

    def test_user_name_login(self):
        request = self.client.post('/account/api-token-auth/',
                                   json.dumps({'username': 'admin', 'password': '123456'}),
                                   content_type="application/json"
                                   )
        print(request.json())