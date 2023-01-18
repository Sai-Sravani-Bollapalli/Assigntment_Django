from rest_framework import serializers
from  .models import Student

class StudentSerializer (serializers.Serializer):
    name = serializers.CharField()
    contact = serializers.CharField()
    address = serializers.CharField()
