from django.db import models

# Create your models here.

class teacher(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    class Meta:
        db_table="teacher_info"


class stud(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    address=models.CharField(max_length=50)
    teach=models.ForeignKey(teacher,on_delete=models.CASCADE)
    class Meta:
        db_table="stud_info"

class college (models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contct=models.IntegerField()
    students=models.ManyToManyField(stud)
    teachers=models.ManyToManyField(teacher)
    def __str__(self):
        return self.name
    def __str__(self):
        return self.name

    class Meta:
        db_table="college_info"

#teacher and student  (one to many)
#college and teacher  (many to many)
#college and student (many to many)
