from django.urls import path
from .views import LeadCreateView, LeadCheckView, LeadUpdateView

urlpatterns = [
    path("leads/create/", LeadCreateView.as_view()),
    path("leads/check/", LeadCheckView.as_view()),
    path("leads/<int:pk>/update/", LeadUpdateView.as_view()),
]