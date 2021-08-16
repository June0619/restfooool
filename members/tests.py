from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from rest_framework import status
import random as r
import string as s


class MembersTest(TestCase):

    def test_get_list(self):
        # given
        c = Client()

        # 랜덤하게 member 객체 주입
        test_case = r.randint(1, 5)
        letters = s.ascii_letters + s.digits

        while test_case > 0:
            random_username = ''.join(r.choice(letters) for i in range(6))
            User.objects.create_user(random_username)

            test_case -= 1

        # when
        response = c.get('/members/')

        # then
        # User 객체 전체 row 수와 동일한 숫자의 json 객체를 반환해야 함
        members_count = User.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], members_count)

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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertURLEqual(response.headers.get('Location'), 'http://testserver/members/' + str(created_user_id) + '/')
