from student.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teacher', teachertVset, basename='teacher')
router.register(r'college', collegeVset, basename='college')
router.register(r'student', StudentVset, basename='students')

urlpatterns = router.urls