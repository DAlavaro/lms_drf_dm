# app/lms/views.py
from rest_framework import viewsets, generics

from app.lms.models import Course, Lesson
from app.lms.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonBaseAPIView:
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(LessonBaseAPIView, generics.CreateAPIView):
    pass


class LessonListAPIView(LessonBaseAPIView, generics.ListAPIView):
    pass


class LessonRetrieveAPIView(LessonBaseAPIView, generics.RetrieveAPIView):
    pass


class LessonUpdateAPIView(LessonBaseAPIView, generics.UpdateAPIView):
    pass


class LessonDestroyAPIView(LessonBaseAPIView, generics.DestroyAPIView):
    pass
