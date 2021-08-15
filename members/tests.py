from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase


class MembersTest(TestCase):

    def test_create(self):
        # given
        c = Client()
        post_body = {
            'username': 'testUser',
            'password': '1234',
            'email': 'testEmail@email.com'
        }

        # when
        response = c.post('/members/', post_body)

        # then
        # post 메서드로 생성 요청이 들어왔으니 status 201과 함께 Location 헤더 영역에 리소스 위치가 리턴되어야 함
        created_user_id = User.objects.get(username='testUser').id
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers.get('Location'), '/members/'+created_user_id)