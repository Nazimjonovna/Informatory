import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from drf_yasg.utils import swagger_auto_schema

from .serializers import ClientSerializer, UserSerializer, ClientGetSerializer
from .models import User, Clients

# Create your views here.
class Clientview(APIView):
    serializer_class = ClientGetSerializer
    queryset = Clients

    def post(self,request, email, *args, **kwargs):
        user = Clients.objects.filter(email = email).first()
        
        serialized_user = serializers.serialize('json', [user]) 

        return Response(serialized_user, content_type='application/json')


class ClientPostView(APIView):
    serializer_class = ClientSerializer
    queryset = Clients

    @swagger_auto_schema(request_body=ClientSerializer)
    def post(self, request):
        serializers = ClientSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                "status":"200.OK",
                "data":serializers.data
            })
        else:
            return Response({
                "status": "400 Bad Request",
                "errors": serializers.errors
            })
            
    
class ClientsGetView(APIView):
    serializer_class = ClientSerializer
    queryset = Clients

    def get(self, request):
        cliens = Clients.objects.all()
        serializer = ClientSerializer(cliens, many = True)
        return Response(serializer.data)
    
class LoginWorkersView(APIView):
    serializer = UserSerializer
    queryset = User

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username = username, password = password)
        if user.exists():
            serializers = UserSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)



# serialized_user = {
#             'id': user.id,
#             'name':user.name,
#             'surname':user.surname,
#             'father_name':user.father_name, 
#             'email':user.email,
#             'date':user.date,
#             'diploma':user.diploma,
#             'picture':user.picture,
#             'phone':user.phone,
#             'pasport_seria':user.pasport_seria,
#             'pasport_raqam':user.pasport_raqam,
#             'university':user.university,
#             'faculty':user.faculty,
#         }
#         json_data = json.dumps(serialized_user)  # Convert the dictionary to JSON

#         return Response(json_data, content_type='application/json')

# class Clientview(APIView):
#     serializer_class = ClientGetSerializer
#     queryset = Clients

#     @swagger_auto_schema(request_body=ClientSerializer)
#     def post(self, request):
#         email = request.data['email']
#         user = Clients.objects.filter(email=email)
#         print(user)
#         if user:
#             serializer = ClientSerializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"user" : user, 'data' :serializer.data})
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(
#                 {
#                     "status": "400 Bad Request",
#                     "errors": {"non_field_errors": ["User not found"]}
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )