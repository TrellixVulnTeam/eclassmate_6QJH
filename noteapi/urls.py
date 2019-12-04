from django.urls import path, include
from rest_framework import routers

from .views import NoteSerializerViewSet

router = routers.DefaultRouter()
router.register('note', NoteSerializerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
