from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# router.register('school', SchoolViewSet)
# router.register('classroom', ClassroomViewSet)
# router.register('teacher', TeacherViewSet)
# router.register('student', StudentViewSet)

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
