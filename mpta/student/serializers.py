from rest_framework.serializers import ModelSerializer
from student.models import *

class teacher_seri(ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'


class student_seri(ModelSerializer):
    class Meta:
        model = stud
        fields = '__all__'


class college_seri(ModelSerializer):
    class Meta:
        model = college
        fields = '__all__'





