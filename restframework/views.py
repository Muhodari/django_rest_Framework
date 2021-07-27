from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# from .serializers import StudentSerializer
# from .models import Student
#

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'no_of_years': 10,
        }

        return Response(data)

    # def post(self, request, *args, **kwargs):
    #     serializer = StudentSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
