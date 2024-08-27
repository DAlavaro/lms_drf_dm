# app/users/urls.py
from rest_framework.routers import DefaultRouter
from app.users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = []
urlpatterns += router.urls
