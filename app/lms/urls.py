# app/lms/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urls import app_name

from app.lms.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = 'lms'

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view()),
    path('lessons/create/', LessonCreateAPIView.as_view()),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view()),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view()),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view()),
]

router = DefaultRouter()
router.register('courses', CourseViewSet)
urlpatterns += router.urls
