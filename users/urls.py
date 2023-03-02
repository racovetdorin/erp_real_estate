from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]
