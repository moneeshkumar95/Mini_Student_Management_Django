from django.forms import ModelForm
from .models import *

class Create_Student(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Add_m(ModelForm):
    class Meta:
        model = Add_Mark
        fields = '__all__'