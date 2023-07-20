from rest_framework import serializers
from .models import User, Clients, University, Consulting


# Serializer for loginpage
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# Serializer for add new_clients
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = (
        'consulting', 'university', 'name', 'surname', 'father_name', 'faculty', 'diploma', 'certificates', "picture",
        'email', 'phone', "date", "pasport_seria", "pasport_raqam", "study_time")


# Serializer for search one student which is need
class ClientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('email',)


# Serializer to get students for university without contacts
class GetUniverView(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('name', 'surname', 'father_name', 'faculty', 'diploma', 'certificates')


# Serializer for add new universities
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


# Serializer for get all consultings's data
class ConsultingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulting
        fields = "__all__"


# Serializer for get one conssulting's data
class GetConsultingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulting
        fields = ('place',)


# Serializer for get all clients for one consulting
class GetConsultClients(serializers.ModelSerializer):
    class Meta:
        model = Consulting
        fields = ('ID_raqam',)


class GetUniverClients(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('ID_raqam',)
