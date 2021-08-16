from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from members.serializers import MemberSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer

# 기존방식의 함수형 뷰가 작동 하지 않음
# serializer 공식문서를 조금 더 학습해야 할 듯

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def member_list(request):
#     if request.method == 'GET':
#         members = User.objects.all()
#         serializer = MemberSerializer(members, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         print('POST')
#
#
# @csrf_exempt
# @api_view(['GET'])
# def member_detail(request, member_id):
#     try:
#         member = User.objects.get(id=member_id)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = MemberSerializer(member)
#         return Response(serializer.data)
#
#
# @api_view(['POST'])
# def member_create(request):
#     username = request.POST.get('username', None)
#     password = request.POST.get('password', None)
#     email = request.POST.get('email', None)
#     new_user = User.objects.create_user(username, password, email)
#
#     new_user.save()
#
#     return Response(status=status.HTTP_201_CREATED, headers={'Location': ''})
