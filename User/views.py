import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_protect

from .serializers import ClientSerializer, UserSerializer, ClientGetSerializer, GetUniverView, UniversitySerializer, ConsultingSerializer, GetConsultingSerializer
from .models import User, Clients, University, Consulting

# Create your views here.

# API for get one student with search by email
class Clientview(APIView):
    serializer_class = ClientGetSerializer
    queryset = Clients

    def post(self,request, email, *args, **kwargs):
        user = Clients.objects.filter(email = email).first()
        if user:
            serialized_user = serializers.serialize('json', [user]) 
            return Response(serialized_user, content_type='application/json')
        else:
            return Response("Bunday student mavjud emas!")

# API for post(add) new student
class ClientPostView(APIView):
    serializer_class = ClientSerializer
    queryset = Clients

    @swagger_auto_schema(request_body=ClientSerializer)
    def post(self, request):
        university = request.data.get('university')
        faculty = request.data.get('faculty')
        study_time = request.data.get('study_time')
        if University.objects.filter(name = university, faculty = faculty, time_study = study_time).exists():
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
        else:
            return Response("Bunday universitet yoq")
            
# API for get all students for consult
class ClientsGetView(APIView):
    serializer_class = ClientSerializer
    queryset = Clients

    def get(self, request):
        cliens = Clients.objects.all()
        serializer = ClientSerializer(cliens, many = True)
        return Response(serializer.data)

# API for loginpage   
class LoginWorkersView(APIView):
    serializer = UserSerializer
    queryset = User

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        ID_raqam = request.data['ID_raqam']
        password = request.data['password']
        user = User.objects.filter(ID_raqam = ID_raqam, password = password)
        if user.exists():
            serializers = UserSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response("Bunday foydalanuvchi topilmadi(")

# API for get student for univer(without contacts)
class UniverGetView(APIView):
    serializer = GetUniverView
    queryset = Clients

    def get(self, request):
        quiz = Clients.objects.all()
        serializer = GetUniverView(quiz, many=True)
        return Response(serializer.data)

# API to add new universities
class UniversityView(APIView):
    serializer = UniversitySerializer
    queryset = University

    @swagger_auto_schema(request_body=UniversitySerializer)
    def post(self, request):
        serializers = UniversitySerializer(data=request.data)
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
        
# API for choise field of universities
class UniversityGet(APIView):
    def get(self, request):
        univer = University.objects.all()
        serializer = UniversitySerializer(univer, many=True)
        return Response(serializer.data)
    

# API for get all consultings
class GetConsultings(APIView):
    serializer_class = ConsultingSerializer
    queryset = Consulting

    def get(self, request):
        data = Consulting.objects.all()
        serializer = ConsultingSerializer(data, many = True)
        return Response(serializer.data)
        
# API for get one consulting data
class GetConsulting(APIView):
    serializer_class = ConsultingSerializer
    queryset = Consulting

    @swagger_auto_schema(request_body=GetConsultingSerializer)
    def post(self, request):
        place = request.data['place']
        try:
            consult = Consulting.objects.get(place=place)
            serializer = ConsultingSerializer(consult)
            return Response(serializer.data)
        except Consulting.DoesNotExist:
            return Response("Bunday Consulting hozircha mavjud emas", status=status.HTTP_404_NOT_FOUND)



