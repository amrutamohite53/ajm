from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from student.models import *
from student.serializers import *
# Create your views here.
class StudentVset(ModelViewSet):
    queryset = stud.objects.all()
    serializer_class = student_seri

class collegeVset(ModelViewSet):
    queryset = college.objects.all()
    serializer_class = college_seri

class teachertVset(ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = teacher_seri