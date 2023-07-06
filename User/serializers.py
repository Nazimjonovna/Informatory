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
        fields = "__all__"

# Serializer for search one student which is need
class ClientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('email', )

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