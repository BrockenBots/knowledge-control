from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from main.models import *
from main.serializers import *


# Create your views here.

class AllUserTestAPIView(generics.ListAPIView):
    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id'))
            category_id = Profile.objects.filter(id=user_id).values()[0]['category_id']
            # category_id = int(request.GET.get('category_id'))
            all_tests = Test.objects.filter(category_id=category_id)
            user_results = [result['test_id'] for result in UserResult.objects.filter(user_id=user_id).values()]
            queryset = all_tests.exclude(id__in=user_results).values()
            return Response(data={'tests':queryset}, status=status.HTTP_200_OK)
        except:
            return Response(data={'user_id':'int'}, status=status.HTTP_400_BAD_REQUEST)


class AuthorizationUserAPIView(views.APIView):
    def get(self, request):
            try:
                username = request.GET.get('username')
                password = request.GET.get('password')
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                profile = Profile.objects.get(user=user.id)
                return Response({'user_data': {
                    'id': profile.id,
                    'category_id': profile.category_id,
                }}, status=status.HTTP_200_OK)

            return Response(data={'Error':'User is unauthorized'},status=status.HTTP_401_UNAUTHORIZED)


class TestAPIView(generics.ListAPIView):
    def get(self, request):
        try:
            test_id = request.GET.get('test_id')
            test = Test.objects.filter(id=test_id).values()[0]
            questions = Question.objects.filter(test_id=test_id).values()
            answers = [Answer.objects.filter(question_id=i['id']).values() for i in questions]
            data = {**test,
                    'questions':[{**i, 'answers': [answers[ind][i] for i in [*range(len(answers[ind]))]]} for ind, i
                                 in enumerate(questions.values())]}
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(data={'test_id':'int'}, status=status.HTTP_400_BAD_REQUEST)


class PushResultAPIView(generics.CreateAPIView):
    def post(self, request):
        serializer = UserResultSerializer(data=request.POST)
        print(request.POST)
        if serializer.is_valid():
            user = request.POST.get('user')
            test = request.POST.get('test')
            UserResult.objects.filter(user=user, test=test).delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
