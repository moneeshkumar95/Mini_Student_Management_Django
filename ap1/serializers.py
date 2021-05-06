from rest_framework import serializers
from . models import *

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AddmarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Add_Mark
        fields = '__all__'
