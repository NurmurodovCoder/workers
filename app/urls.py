from django.urls import path
from .views import PersonRetrieveAPIView, PersonCreateListAPIView

urlpatterns = [
    path('person/', PersonCreateListAPIView.as_view()),
    path('person/<int:id>/', PersonRetrieveAPIView.as_view()),
]
