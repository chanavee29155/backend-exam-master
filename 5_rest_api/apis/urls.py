from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1.school import SchoolViewSet, ClassroomViewSet
from apis.views.v1.teacher import TeacherViewSet
from apis.views.v1.student import StudentViewSet


router = DefaultRouter()

router.register(r'school', SchoolViewSet, basename='school')
router.register(r'classroom', ClassroomViewSet, basename='classroom')
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentViewSet, basename='student')


api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
